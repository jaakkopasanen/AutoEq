# Sony MDR-1RBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.5; 25 -6.5; 28 -7.6; 31 -8.6; 34 -9.4; 37 -10.1; 41 -10.9; 45 -11.6; 49 -12.1; 54 -12.6; 60 -13.1; 66 -13.8; 72 -14.3; 79 -14.7; 87 -15.3; 96 -15.2; 106 -14.3; 116 -13.5; 128 -13.6; 141 -13.7; 155 -13.8; 170 -10.1; 187 -10.0; 206 -7.8; 227 -5.1; 249 -1.9; 274 -1.0; 302 -0.5; 332 -0.5; 365 -1.0; 402 -2.6; 442 -4.5; 486 -5.2; 535 -4.2; 588 -3.0; 647 -3.9; 712 -4.9; 783 -3.6; 861 -4.8; 947 -5.9; 1042 -5.7; 1146 -5.4; 1261 -6.9; 1387 -9.1; 1526 -11.4; 1678 -12.9; 1846 -14.6; 2031 -14.3; 2234 -14.3; 2457 -11.0; 2703 -7.6; 2973 -4.7; 3270 -4.5; 3597 -6.2; 3957 -7.1; 4353 -5.5; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -10.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1RBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1RBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 1.32 | -9.1 dB |
| Peaking | 140 Hz  | 3.64 | -5.7 dB |
| Peaking | 1959 Hz | 2.99 | -9.6 dB |
| Peaking | 5567 Hz | 2.93 | 7.2 dB  |
| Peaking | 310 Hz  | 2.41 | 7.3 dB  |
| Peaking | 678 Hz  | 1.65 | 2.6 dB  |
| Peaking | 6565 Hz | 7.54 | 2.1 dB  |
| Peaking | 9068 Hz | 5.38 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -9.1 dB |
| Peaking | 250 Hz   | 1.41 | 5.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1RBT/Sony%20MDR-1RBT.png)