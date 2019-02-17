# Beyerdynamic DT 990 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.4; 31 -3.0; 34 -3.6; 37 -4.1; 41 -4.7; 45 -5.2; 49 -5.7; 54 -6.2; 60 -6.9; 66 -7.4; 72 -7.7; 79 -7.3; 87 -7.9; 96 -8.9; 106 -9.4; 116 -9.7; 128 -9.9; 141 -10.1; 155 -10.0; 170 -9.7; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.6; 274 -8.1; 302 -7.5; 332 -6.9; 365 -6.1; 402 -5.5; 442 -5.0; 486 -4.4; 535 -4.3; 588 -3.8; 647 -3.4; 712 -2.9; 783 -2.7; 861 -3.0; 947 -3.7; 1042 -4.4; 1146 -4.7; 1261 -5.1; 1387 -5.5; 1526 -5.7; 1678 -5.7; 1846 -6.1; 2031 -6.1; 2234 -5.0; 2457 -4.4; 2703 -4.8; 2973 -5.2; 3270 -5.4; 3597 -4.7; 3957 -4.6; 4353 -5.8; 4788 -5.8; 5267 -4.8; 5793 -7.8; 6373 -10.8; 7010 -9.1; 7711 -9.1; 8482 -12.4; 9330 -12.6; 10263 -7.3; 11289 -5.2; 12418 -7.4; 13660 -6.3; 15026 -4.4; 16529 -6.8; 18182 -9.7; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  1.68 | 3.9 dB  |
| Peaking | 122 Hz   |  0.77 | -5.5 dB |
| Peaking | 233 Hz   |  1.61 | -2.5 dB |
| Peaking | 8306 Hz  |  1.4  | -7.5 dB |
| Peaking | 19195 Hz |  1    | -6.8 dB |
| Peaking | 762 Hz   |  2.32 | 2.1 dB  |
| Peaking | 1659 Hz  |  1.54 | -1.8 dB |
| Peaking | 5219 Hz  | 14.92 | 1.8 dB  |
| Peaking | 9185 Hz  |  9.15 | -3.0 dB |
| Peaking | 10825 Hz |  6.62 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20990%20250%20Ohm/Beyerdynamic%20DT%20990%20250%20Ohm.png)