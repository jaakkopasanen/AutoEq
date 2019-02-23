# Beyerdynamic DT 990 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.4; 31 -3.0; 34 -3.6; 37 -4.1; 41 -4.7; 45 -5.2; 49 -5.7; 54 -6.2; 60 -6.9; 66 -7.4; 72 -7.7; 79 -7.3; 87 -8.0; 96 -8.9; 106 -9.4; 116 -9.7; 128 -9.9; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.6; 274 -8.1; 302 -7.5; 332 -6.9; 365 -6.1; 402 -5.6; 442 -5.1; 486 -4.4; 535 -4.4; 588 -3.8; 647 -3.4; 712 -2.9; 783 -2.7; 861 -3.0; 947 -3.7; 1042 -4.4; 1146 -4.8; 1261 -5.1; 1387 -5.5; 1526 -5.7; 1678 -5.7; 1846 -6.1; 2031 -6.1; 2234 -5.0; 2457 -4.5; 2703 -4.8; 2973 -5.2; 3270 -5.5; 3597 -4.7; 3957 -4.6; 4353 -5.8; 4788 -5.8; 5267 -4.9; 5793 -7.8; 6373 -10.8; 7010 -9.1; 7711 -9.1; 8482 -12.4; 9330 -12.7; 10263 -7.4; 11289 -6.7; 12418 -7.4; 13660 -6.8; 15026 -6.7; 16529 -7.1; 18182 -9.7; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.74 | 6.6 dB  |
| Peaking | 149 Hz   | 0.72 | -3.8 dB |
| Peaking | 698 Hz   | 0.99 | 4.1 dB  |
| Peaking | 3376 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8700 Hz  | 2.8  | -6.5 dB |
| Peaking | 1817 Hz  | 4.67 | -0.4 dB |
| Peaking | 5138 Hz  | 6.59 | 2.0 dB  |
| Peaking | 6191 Hz  | 7.02 | -3.8 dB |
| Peaking | 10898 Hz | 5.8  | 2.0 dB  |
| Peaking | 21475 Hz | 0.55 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20990%20250%20Ohm/Beyerdynamic%20DT%20990%20250%20Ohm.png)