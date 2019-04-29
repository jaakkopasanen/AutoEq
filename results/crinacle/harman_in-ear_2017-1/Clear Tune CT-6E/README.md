# Clear Tune CT-6E
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.2; 79 -7.6; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.2; 128 -9.5; 141 -9.9; 155 -10.2; 170 -10.3; 187 -10.4; 206 -10.5; 227 -10.5; 249 -10.5; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.5; 535 -8.0; 588 -7.3; 647 -6.6; 712 -5.5; 783 -4.1; 861 -2.2; 947 -0.5; 1042 -0.5; 1146 -3.4; 1261 -6.4; 1387 -8.3; 1526 -9.7; 1678 -11.1; 1846 -12.0; 2031 -11.1; 2234 -9.0; 2457 -6.7; 2703 -5.1; 2973 -4.6; 3270 -4.8; 3597 -5.0; 3957 -6.1; 4353 -5.4; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -15.1; 16529 -14.7; 18182 -9.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 233 Hz   | 0.61 | -4.3 dB  |
| Peaking | 971 Hz   | 2.67 | 7.8 dB   |
| Peaking | 1765 Hz  | 2.64 | -6.4 dB  |
| Peaking | 5596 Hz  | 2.19 | 6.8 dB   |
| Peaking | 15962 Hz | 2.19 | -10.6 dB |
| Peaking | 26 Hz    | 0.86 | 1.7 dB   |
| Peaking | 2847 Hz  | 1.33 | -2.4 dB  |
| Peaking | 2871 Hz  | 2.75 | 4.6 dB   |
| Peaking | 7922 Hz  | 6.26 | -1.3 dB  |
| Peaking | 13111 Hz | 5.12 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-6E/Clear%20Tune%20CT-6E.png)