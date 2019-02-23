# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.2; 49 -1.6; 54 -2.3; 60 -2.9; 66 -3.1; 72 -2.7; 79 -3.0; 87 -3.6; 96 -3.9; 106 -4.1; 116 -4.2; 128 -4.2; 141 -4.2; 155 -4.2; 170 -3.9; 187 -3.7; 206 -3.5; 227 -4.1; 249 -5.3; 274 -5.0; 302 -4.6; 332 -4.8; 365 -5.4; 402 -6.2; 442 -6.4; 486 -6.6; 535 -6.8; 588 -6.5; 647 -6.3; 712 -6.1; 783 -5.9; 861 -5.9; 947 -5.5; 1042 -5.6; 1146 -5.7; 1261 -6.4; 1387 -6.5; 1526 -7.5; 1678 -8.1; 1846 -8.2; 2031 -8.2; 2234 -8.7; 2457 -8.8; 2703 -9.9; 2973 -10.7; 3270 -10.6; 3597 -9.7; 3957 -8.6; 4353 -11.0; 4788 -10.5; 5267 -5.8; 5793 -1.5; 6373 -1.6; 7010 -4.9; 7711 -6.7; 8482 -9.3; 9330 -12.6; 10263 -12.0; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.09 | 5.3 dB  |
| Peaking | 2976 Hz | 1.65 | -4.0 dB |
| Peaking | 4675 Hz | 4.41 | -5.5 dB |
| Peaking | 6001 Hz | 3.18 | 7.4 dB  |
| Peaking | 9567 Hz | 3.9  | -7.5 dB |
| Peaking | 32 Hz   | 1.11 | 1.9 dB  |
| Peaking | 198 Hz  | 2.28 | 2.3 dB  |
| Peaking | 204 Hz  | 0.13 | -1.3 dB |
| Peaking | 325 Hz  | 3.09 | 1.8 dB  |
| Peaking | 939 Hz  | 1.51 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)