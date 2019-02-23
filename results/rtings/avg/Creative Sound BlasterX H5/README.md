# Creative Sound BlasterX H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.1; 25 -1.9; 28 -1.8; 31 -1.9; 34 -1.8; 37 -1.6; 41 -1.1; 45 -0.8; 49 -0.9; 54 -1.4; 60 -2.4; 66 -3.4; 72 -4.3; 79 -5.3; 87 -6.1; 96 -6.9; 106 -7.6; 116 -8.1; 128 -8.6; 141 -9.1; 155 -9.4; 170 -9.7; 187 -9.9; 206 -10.1; 227 -10.2; 249 -10.3; 274 -10.2; 302 -9.6; 332 -9.7; 365 -9.4; 402 -9.0; 442 -8.6; 486 -8.2; 535 -7.5; 588 -6.8; 647 -5.9; 712 -4.7; 783 -3.5; 861 -2.4; 947 -1.3; 1042 -0.7; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -1.2; 1678 -2.1; 1846 -3.5; 2031 -5.3; 2234 -6.6; 2457 -7.1; 2703 -7.8; 2973 -8.3; 3270 -9.3; 3597 -8.2; 3957 -3.4; 4353 -1.4; 4788 -0.6; 5267 -5.6; 5793 -7.6; 6373 -6.9; 7010 -8.1; 7711 -9.1; 8482 -9.3; 9330 -8.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound BlasterX H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound BlasterX H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.98 | 3.5 dB  |
| Peaking | 49 Hz   | 1.14 | 5.4 dB  |
| Peaking | 230 Hz  | 0.5  | -4.2 dB |
| Peaking | 1128 Hz | 1.43 | 7.5 dB  |
| Peaking | 4598 Hz | 6.88 | 6.4 dB  |
| Peaking | 1163 Hz | 6.96 | -1.2 dB |
| Peaking | 1601 Hz | 3.25 | 2.2 dB  |
| Peaking | 3502 Hz | 1.91 | -5.7 dB |
| Peaking | 3988 Hz | 3.67 | 6.1 dB  |
| Peaking | 8188 Hz | 2.78 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20BlasterX%20H5/Creative%20Sound%20BlasterX%20H5.png)