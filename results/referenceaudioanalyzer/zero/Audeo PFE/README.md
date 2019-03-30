# Audeo PFE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.9; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.1; 41 -11.1; 45 -11.1; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.1; 72 -11.1; 79 -11.2; 87 -11.2; 96 -11.1; 106 -11.1; 116 -11.1; 128 -11.1; 141 -11.0; 155 -10.7; 170 -10.8; 187 -10.7; 206 -10.5; 227 -10.4; 249 -10.3; 274 -10.1; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.2; 442 -9.1; 486 -9.1; 535 -8.9; 588 -8.5; 647 -8.2; 712 -7.9; 783 -7.6; 861 -7.3; 947 -7.1; 1042 -6.9; 1146 -6.7; 1261 -6.4; 1387 -6.2; 1526 -5.9; 1678 -5.7; 1846 -5.5; 2031 -5.2; 2234 -4.9; 2457 -5.4; 2703 -6.1; 2973 -6.2; 3270 -5.9; 3597 -5.6; 3957 -5.5; 4353 -5.3; 4788 -4.4; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.33 | -3.6 dB |
| Peaking | 195 Hz  | 0.34 | -3.5 dB |
| Peaking | 1946 Hz | 1.5  | 1.5 dB  |
| Peaking | 5887 Hz | 3.36 | 6.6 dB  |
| Peaking | 17 Hz   | 0.73 | -0.7 dB |
| Peaking | 1023 Hz | 3.38 | 0.2 dB  |
| Peaking | 8155 Hz | 4.88 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeo%20PFE/Audeo%20PFE.png)