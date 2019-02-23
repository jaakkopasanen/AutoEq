# iHarmonix Platinum ev-Series
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -13.2; 25 -13.2; 28 -13.2; 31 -13.2; 34 -13.2; 37 -13.2; 41 -13.2; 45 -13.2; 49 -13.3; 54 -13.3; 60 -13.3; 66 -13.5; 72 -13.6; 79 -13.7; 87 -13.8; 96 -13.9; 106 -13.8; 116 -13.7; 128 -13.7; 141 -13.5; 155 -13.3; 170 -13.0; 187 -12.7; 206 -12.3; 227 -11.7; 249 -11.3; 274 -10.7; 302 -10.0; 332 -9.6; 365 -8.9; 402 -8.3; 442 -7.4; 486 -6.8; 535 -6.3; 588 -5.3; 647 -4.8; 712 -4.3; 783 -3.5; 861 -3.5; 947 -3.4; 1042 -3.5; 1146 -3.8; 1261 -3.8; 1387 -4.3; 1526 -4.7; 1678 -5.0; 1846 -5.1; 2031 -5.1; 2234 -5.4; 2457 -5.2; 2703 -5.2; 2973 -2.7; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.4; 4788 -9.0; 5267 -10.1; 5793 -4.1; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iHarmonix Platinum ev-Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix Platinum ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.37 | -5.7 dB |
| Peaking | 132 Hz   | 0.39 | -6.6 dB |
| Peaking | 851 Hz   | 0.81 | 4.1 dB  |
| Peaking | 3506 Hz  | 3.57 | 6.7 dB  |
| Peaking | 21538 Hz | 2.29 | 2.1 dB  |
| Peaking | 4073 Hz  | 7.8  | 2.9 dB  |
| Peaking | 5120 Hz  | 4.35 | -7.3 dB |
| Peaking | 6291 Hz  | 3.12 | 7.2 dB  |
| Peaking | 6738 Hz  | 0.68 | -0.4 dB |
| Peaking | 7554 Hz  | 3.5  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iHarmonix%20Platinum%20ev-Series/iHarmonix%20Platinum%20ev-Series.png)