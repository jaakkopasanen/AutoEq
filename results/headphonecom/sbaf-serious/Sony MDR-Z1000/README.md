# Sony MDR-Z1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.4; 72 -2.2; 79 -3.0; 87 -3.7; 96 -4.0; 106 -4.5; 116 -5.2; 128 -6.1; 141 -6.7; 155 -6.7; 170 -6.1; 187 -6.0; 206 -5.7; 227 -5.3; 249 -4.8; 274 -3.8; 302 -4.8; 332 -5.7; 365 -6.3; 402 -6.7; 442 -6.9; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.2; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -6.4; 1146 -6.6; 1261 -7.2; 1387 -8.2; 1526 -9.5; 1678 -10.5; 1846 -10.7; 2031 -10.3; 2234 -8.4; 2457 -7.0; 2703 -5.6; 2973 -4.0; 3270 -2.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -13.6; 10263 -9.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.62 | 6.9 dB   |
| Peaking | 276 Hz  | 5.83 | 2.5 dB   |
| Peaking | 1923 Hz | 1.67 | -6.7 dB  |
| Peaking | 4643 Hz | 0.7  | 7.4 dB   |
| Peaking | 9201 Hz | 3.36 | -10.2 dB |
| Peaking | 39 Hz   | 2.67 | -1.1 dB  |
| Peaking | 62 Hz   | 2.44 | 1.3 dB   |
| Peaking | 142 Hz  | 3.88 | -1.6 dB  |
| Peaking | 473 Hz  | 4.2  | -0.8 dB  |
| Peaking | 1099 Hz | 4.52 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Z1000/Sony%20MDR-Z1000.png)