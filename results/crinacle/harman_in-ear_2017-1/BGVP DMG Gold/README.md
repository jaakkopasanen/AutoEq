# BGVP DMG Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.3; 25 -10.6; 28 -11.0; 31 -11.3; 34 -11.5; 37 -11.7; 41 -11.9; 45 -12.0; 49 -12.2; 54 -12.3; 60 -12.5; 66 -12.6; 72 -12.8; 79 -13.1; 87 -13.2; 96 -13.5; 106 -13.6; 116 -13.7; 128 -13.7; 141 -13.6; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.8; 227 -12.4; 249 -11.9; 274 -11.4; 302 -10.8; 332 -10.1; 365 -9.5; 402 -8.9; 442 -8.3; 486 -7.6; 535 -7.0; 588 -6.3; 647 -5.7; 712 -4.9; 783 -4.1; 861 -3.4; 947 -3.1; 1042 -3.1; 1146 -3.2; 1261 -3.4; 1387 -3.4; 1526 -3.2; 1678 -3.0; 1846 -2.8; 2031 -2.3; 2234 -1.8; 2457 -1.5; 2703 -1.9; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -2.7; 4788 -4.5; 5267 -5.4; 5793 -5.6; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -8.5; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -16.2; 16529 -21.9; 18182 -21.0; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.41 | -3.8 dB  |
| Peaking | 160 Hz   | 0.48 | -6.2 dB  |
| Peaking | 911 Hz   | 1.09 | 3.3 dB   |
| Peaking | 3098 Hz  | 0.77 | 5.4 dB   |
| Peaking | 17491 Hz | 1.22 | -17.9 dB |
| Peaking | 5517 Hz  | 3.15 | -1.8 dB  |
| Peaking | 6634 Hz  | 8.18 | 3.5 dB   |
| Peaking | 12946 Hz | 3.09 | 4.6 dB   |
| Peaking | 15587 Hz | 3.53 | -4.3 dB  |
| Peaking | 19189 Hz | 3.76 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DMG%20Gold/BGVP%20DMG%20Gold.png)