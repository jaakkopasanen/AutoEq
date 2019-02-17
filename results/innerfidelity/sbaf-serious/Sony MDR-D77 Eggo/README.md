# Sony MDR-D77 Eggo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.1; 54 -2.8; 60 -3.4; 66 -3.9; 72 -4.3; 79 -4.7; 87 -5.0; 96 -5.3; 106 -5.4; 116 -5.2; 128 -5.0; 141 -5.2; 155 -5.4; 170 -5.1; 187 -5.0; 206 -5.0; 227 -4.4; 249 -4.0; 274 -3.8; 302 -3.1; 332 -3.1; 365 -3.9; 402 -3.2; 442 -3.1; 486 -3.8; 535 -4.5; 588 -5.0; 647 -5.6; 712 -6.0; 783 -6.0; 861 -6.4; 947 -6.4; 1042 -6.8; 1146 -6.9; 1261 -5.6; 1387 -4.2; 1526 -6.4; 1678 -8.0; 1846 -8.3; 2031 -7.7; 2234 -6.6; 2457 -4.7; 2703 -3.4; 2973 -1.7; 3270 -0.8; 3597 -1.8; 3957 -2.2; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-D77 Eggo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-D77 Eggo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.69 | 6.5 dB  |
| Peaking | 351 Hz  | 1.09 | 3.4 dB  |
| Peaking | 1924 Hz | 3.5  | -3.1 dB |
| Peaking | 3216 Hz | 2    | 4.8 dB  |
| Peaking | 5415 Hz | 2.21 | 6.0 dB  |
| Peaking | 463 Hz  | 6.57 | 0.8 dB  |
| Peaking | 1220 Hz | 1.63 | -1.3 dB |
| Peaking | 1371 Hz | 6.12 | 3.5 dB  |
| Peaking | 6500 Hz | 6.74 | 2.4 dB  |
| Peaking | 7959 Hz | 2.03 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-D77%20Eggo/Sony%20MDR-D77%20Eggo.png)