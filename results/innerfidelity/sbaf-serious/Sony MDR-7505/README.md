# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.6; 96 -1.5; 106 -2.1; 116 -2.1; 128 -2.0; 141 -2.9; 155 -3.7; 170 -3.6; 187 -3.9; 206 -3.9; 227 -3.9; 249 -3.9; 274 -3.5; 302 -3.8; 332 -4.2; 365 -4.8; 402 -4.8; 442 -4.8; 486 -5.6; 535 -6.1; 588 -6.2; 647 -6.8; 712 -6.7; 783 -5.0; 861 -6.0; 947 -6.5; 1042 -6.5; 1146 -5.9; 1261 -5.6; 1387 -5.2; 1526 -4.9; 1678 -4.2; 1846 -3.7; 2031 -3.2; 2234 -3.0; 2457 -2.9; 2703 -2.4; 2973 -3.4; 3270 -3.8; 3597 -3.9; 3957 -3.8; 4353 -4.6; 4788 -3.6; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.16 | 5.8 dB  |
| Peaking | 86 Hz   | 0.75 | 2.3 dB  |
| Peaking | 292 Hz  | 1.79 | 1.9 dB  |
| Peaking | 2454 Hz | 1.27 | 3.7 dB  |
| Peaking | 5790 Hz | 3.16 | 6.2 dB  |
| Peaking | 678 Hz  | 4.16 | -2.6 dB |
| Peaking | 784 Hz  | 2.2  | 2.6 dB  |
| Peaking | 927 Hz  | 3.25 | -2.0 dB |
| Peaking | 8198 Hz | 4.55 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)