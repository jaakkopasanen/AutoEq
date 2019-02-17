# Sony MDR-V600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.3; 54 -3.3; 60 -4.2; 66 -4.7; 72 -5.2; 79 -6.4; 87 -7.3; 96 -7.6; 106 -7.0; 116 -6.6; 128 -7.8; 141 -8.9; 155 -9.6; 170 -9.2; 187 -9.2; 206 -10.0; 227 -10.3; 249 -10.4; 274 -10.3; 302 -10.0; 332 -9.8; 365 -9.5; 402 -9.7; 442 -10.1; 486 -9.4; 535 -9.1; 588 -8.6; 647 -7.2; 712 -7.9; 783 -7.5; 861 -7.3; 947 -7.0; 1042 -6.1; 1146 -5.4; 1261 -4.5; 1387 -4.4; 1526 -5.1; 1678 -5.6; 1846 -5.0; 2031 -3.5; 2234 -2.1; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.0; 3957 -2.5; 4353 -4.4; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.4; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.75 | 6.9 dB  |
| Peaking | 228 Hz  | 0.64 | -3.8 dB |
| Peaking | 465 Hz  | 2.37 | -1.5 dB |
| Peaking | 2826 Hz | 1.43 | 6.2 dB  |
| Peaking | 5768 Hz | 3.43 | 5.8 dB  |
| Peaking | 88 Hz   | 3.69 | -1.3 dB |
| Peaking | 115 Hz  | 7.06 | 1.5 dB  |
| Peaking | 1313 Hz | 4.55 | 1.8 dB  |
| Peaking | 1741 Hz | 5.36 | -1.2 dB |
| Peaking | 9278 Hz | 5.23 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V600/Sony%20MDR-V600.png)