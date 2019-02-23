# Sony MDR-1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.5; 28 -2.4; 31 -3.3; 34 -4.1; 37 -4.7; 41 -5.5; 45 -6.2; 49 -6.8; 54 -7.4; 60 -7.9; 66 -8.4; 72 -9.0; 79 -9.7; 87 -10.3; 96 -10.5; 106 -10.8; 116 -10.8; 128 -10.2; 141 -9.8; 155 -10.6; 170 -9.5; 187 -9.5; 206 -10.2; 227 -10.4; 249 -9.8; 274 -9.6; 302 -8.5; 332 -7.5; 365 -6.2; 402 -5.5; 442 -5.1; 486 -5.4; 535 -5.7; 588 -5.9; 647 -6.6; 712 -7.2; 783 -7.2; 861 -8.0; 947 -8.7; 1042 -9.3; 1146 -9.8; 1261 -10.3; 1387 -11.3; 1526 -12.2; 1678 -12.6; 1846 -12.2; 2031 -11.2; 2234 -9.5; 2457 -7.0; 2703 -5.0; 2973 -2.9; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.19 | 6.1 dB  |
| Peaking | 103 Hz  | 1.01 | -4.5 dB |
| Peaking | 229 Hz  | 2.95 | -3.0 dB |
| Peaking | 1731 Hz | 1.42 | -8.0 dB |
| Peaking | 4061 Hz | 1.06 | 7.9 dB  |
| Peaking | 465 Hz  | 2.67 | 2.2 dB  |
| Peaking | 1035 Hz | 4.13 | -1.0 dB |
| Peaking | 4282 Hz | 6.17 | -1.2 dB |
| Peaking | 6175 Hz | 3.47 | 3.0 dB  |
| Peaking | 8599 Hz | 2.22 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1R/Sony%20MDR-1R.png)