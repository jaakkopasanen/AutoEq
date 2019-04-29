# VSonic Ares
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.3; 25 -14.3; 28 -14.2; 31 -14.0; 34 -13.9; 37 -13.8; 41 -13.6; 45 -13.5; 49 -13.3; 54 -13.1; 60 -13.0; 66 -12.8; 72 -12.8; 79 -12.7; 87 -12.6; 96 -12.6; 106 -12.5; 116 -12.3; 128 -12.2; 141 -12.0; 155 -11.8; 170 -11.5; 187 -11.3; 206 -10.9; 227 -10.6; 249 -10.2; 274 -9.9; 302 -9.5; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.3; 486 -8.0; 535 -7.7; 588 -7.4; 647 -7.1; 712 -6.8; 783 -6.3; 861 -5.9; 947 -5.8; 1042 -5.9; 1146 -6.2; 1261 -6.4; 1387 -6.3; 1526 -5.9; 1678 -5.4; 1846 -5.0; 2031 -4.7; 2234 -4.4; 2457 -4.0; 2703 -3.0; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -5.5; 6373 -7.2; 7010 -6.4; 7711 -8.6; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.5; 15026 -21.0; 16529 -21.6; 18182 -22.5; 20000 -22.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic Ares GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic Ares ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.48 | -6.7 dB  |
| Peaking | 116 Hz   | 0.35 | -5.0 dB  |
| Peaking | 7349 Hz  | 1.87 | -10.1 dB |
| Peaking | 8193 Hz  | 0.43 | 15.1 dB  |
| Peaking | 17351 Hz | 0.35 | -21.3 dB |
| Peaking | 2354 Hz  | 1.08 | -3.0 dB  |
| Peaking | 3316 Hz  | 1.03 | 3.4 dB   |
| Peaking | 5982 Hz  | 8.51 | -3.5 dB  |
| Peaking | 12561 Hz | 4.99 | 5.1 dB   |
| Peaking | 14537 Hz | 3.6  | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20Ares/VSonic%20Ares.png)