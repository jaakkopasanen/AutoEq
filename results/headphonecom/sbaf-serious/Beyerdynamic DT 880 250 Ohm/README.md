# Beyerdynamic DT 880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.3; 31 -1.7; 34 -2.0; 37 -2.3; 41 -2.7; 45 -2.7; 49 -2.6; 54 -2.8; 60 -3.2; 66 -3.8; 72 -4.0; 79 -4.2; 87 -4.9; 96 -5.4; 106 -5.7; 116 -5.9; 128 -6.3; 141 -6.5; 155 -6.7; 170 -7.0; 187 -7.1; 206 -7.1; 227 -7.1; 249 -7.1; 274 -7.1; 302 -6.9; 332 -6.8; 365 -6.6; 402 -6.5; 442 -6.3; 486 -5.8; 535 -5.8; 588 -5.7; 647 -5.6; 712 -5.5; 783 -5.5; 861 -5.6; 947 -5.5; 1042 -5.4; 1146 -4.8; 1261 -4.5; 1387 -4.7; 1526 -5.3; 1678 -5.6; 1846 -5.8; 2031 -5.5; 2234 -5.1; 2457 -4.8; 2703 -5.0; 2973 -5.5; 3270 -6.3; 3597 -6.8; 3957 -7.0; 4353 -5.4; 4788 -4.8; 5267 -7.8; 5793 -10.2; 6373 -9.9; 7010 -7.9; 7711 -9.8; 8482 -11.4; 9330 -10.6; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -9.0; 18182 -10.3; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.96 | 5.7 dB  |
| Peaking | 55 Hz    | 1.57 | 2.6 dB  |
| Peaking | 1526 Hz  | 0.64 | 1.6 dB  |
| Peaking | 8165 Hz  | 1.93 | -4.4 dB |
| Peaking | 19867 Hz | 0.84 | -8.3 dB |
| Peaking | 216 Hz   | 1.59 | -1.0 dB |
| Peaking | 4757 Hz  | 4.69 | 4.3 dB  |
| Peaking | 6268 Hz  | 1.73 | -5.7 dB |
| Peaking | 7054 Hz  | 3.87 | 6.0 dB  |
| Peaking | 11351 Hz | 2.64 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)