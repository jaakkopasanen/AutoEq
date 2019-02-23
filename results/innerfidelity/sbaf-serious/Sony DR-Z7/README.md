# Sony DR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.1; 66 -1.4; 72 -1.9; 79 -2.5; 87 -2.8; 96 -2.9; 106 -2.9; 116 -3.6; 128 -4.6; 141 -5.5; 155 -5.6; 170 -5.3; 187 -6.1; 206 -6.6; 227 -6.6; 249 -6.5; 274 -6.6; 302 -6.5; 332 -6.4; 365 -6.3; 402 -6.3; 442 -6.1; 486 -6.7; 535 -6.8; 588 -6.5; 647 -7.1; 712 -7.9; 783 -8.3; 861 -8.9; 947 -9.4; 1042 -9.9; 1146 -10.4; 1261 -11.2; 1387 -12.4; 1526 -13.6; 1678 -14.9; 1846 -15.8; 2031 -15.8; 2234 -14.9; 2457 -12.6; 2703 -10.7; 2973 -8.5; 3270 -7.4; 3597 -7.1; 3957 -7.0; 4353 -8.3; 4788 -7.6; 5267 -4.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony DR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony DR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.25 | 6.2 dB  |
| Peaking | 180 Hz  | 1.05 | -1.7 dB |
| Peaking | 1840 Hz | 1.36 | -9.7 dB |
| Peaking | 4596 Hz | 6.91 | -2.8 dB |
| Peaking | 5901 Hz | 3.13 | 7.2 dB  |
| Peaking | 952 Hz  | 3.25 | -0.9 dB |
| Peaking | 1758 Hz | 3.13 | 0.9 dB  |
| Peaking | 2240 Hz | 3.7  | -1.5 dB |
| Peaking | 3268 Hz | 2.87 | 2.0 dB  |
| Peaking | 5572 Hz | 0.49 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -9.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20DR-Z7/Sony%20DR-Z7.png)