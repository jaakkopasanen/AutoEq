# iHarmonix Platinum ev-Series
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.8; 25 -14.8; 28 -14.8; 31 -14.8; 34 -14.8; 37 -14.8; 41 -14.8; 45 -14.9; 49 -14.9; 54 -15.0; 60 -15.0; 66 -15.1; 72 -15.2; 79 -15.4; 87 -15.4; 96 -15.5; 106 -15.5; 116 -15.4; 128 -15.3; 141 -15.2; 155 -14.9; 170 -14.6; 187 -14.3; 206 -13.9; 227 -13.4; 249 -13.0; 274 -12.4; 302 -11.7; 332 -11.3; 365 -10.5; 402 -10.0; 442 -9.0; 486 -8.4; 535 -7.9; 588 -6.9; 647 -6.5; 712 -6.0; 783 -5.2; 861 -5.2; 947 -5.0; 1042 -5.1; 1146 -5.4; 1261 -5.5; 1387 -5.9; 1526 -6.3; 1678 -6.6; 1846 -6.7; 2031 -6.8; 2234 -7.0; 2457 -6.9; 2703 -6.8; 2973 -4.4; 3270 -1.5; 3597 -0.5; 3957 -2.0; 4353 -6.0; 4788 -10.7; 5267 -11.7; 5793 -5.7; 6373 -2.6; 7010 -2.5; 7711 -4.7; 8482 -6.8; 9330 -4.9; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iHarmonix Platinum ev-Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix Platinum ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.16 | -9.7 dB  |
| Peaking | 198 Hz  | 0.58 | -4.8 dB  |
| Peaking | 2628 Hz | 1.34 | -9.4 dB  |
| Peaking | 3421 Hz | 1.1  | 11.0 dB  |
| Peaking | 4974 Hz | 4.15 | -11.9 dB |
| Peaking | 852 Hz  | 2.58 | 1.2 dB   |
| Peaking | 1616 Hz | 4.93 | -0.8 dB  |
| Peaking | 5354 Hz | 5.64 | -1.8 dB  |
| Peaking | 6499 Hz | 3.89 | 3.3 dB   |
| Peaking | 8354 Hz | 4.53 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -8.6 dB  |
| Peaking | 250 Hz   | 1.41 | -6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iHarmonix%20Platinum%20ev-Series/iHarmonix%20Platinum%20ev-Series.png)