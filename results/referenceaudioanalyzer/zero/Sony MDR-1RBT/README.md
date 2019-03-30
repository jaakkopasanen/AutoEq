# Sony MDR-1RBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.5; 25 -6.5; 28 -7.7; 31 -8.7; 34 -9.6; 37 -10.3; 41 -11.1; 45 -11.6; 49 -12.1; 54 -12.7; 60 -13.6; 66 -14.6; 72 -15.4; 79 -16.1; 87 -16.4; 96 -16.4; 106 -16.2; 116 -15.8; 128 -15.2; 141 -14.2; 155 -13.0; 170 -11.2; 187 -8.9; 206 -6.6; 227 -4.6; 249 -3.2; 274 -1.7; 302 -0.6; 332 -0.5; 365 -0.5; 402 -1.3; 442 -2.1; 486 -2.9; 535 -3.7; 588 -4.3; 647 -4.6; 712 -4.8; 783 -5.2; 861 -5.5; 947 -5.9; 1042 -6.3; 1146 -6.8; 1261 -7.5; 1387 -8.3; 1526 -9.2; 1678 -9.9; 1846 -10.4; 2031 -10.3; 2234 -9.3; 2457 -7.3; 2703 -5.0; 2973 -3.3; 3270 -3.7; 3597 -4.8; 3957 -4.5; 4353 -2.4; 4788 -0.6; 5267 -0.5; 5793 -1.2; 6373 -5.6; 7010 -8.8; 7711 -10.9; 8482 -12.0; 9330 -11.4; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1RBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1RBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.88 | -6.6 dB |
| Peaking | 128 Hz   | 1.04 | -7.0 dB |
| Peaking | 313 Hz   | 1.17 | 8.3 dB  |
| Peaking | 5211 Hz  | 2.33 | 7.8 dB  |
| Peaking | 8229 Hz  | 2.16 | -7.0 dB |
| Peaking | 38 Hz    | 3.97 | -0.9 dB |
| Peaking | 805 Hz   | 0.96 | 0.9 dB  |
| Peaking | 1930 Hz  | 1.39 | -5.0 dB |
| Peaking | 2939 Hz  | 3.21 | 4.5 dB  |
| Peaking | 11461 Hz | 5.05 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -10.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.9 dB   |
| Peaking | 500 Hz   | 1.41 | 3.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-1RBT/Sony%20MDR-1RBT.png)