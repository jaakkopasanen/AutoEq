# Denon AH-D5000 JMoney Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.8; 25 -2.8; 28 -4.0; 31 -4.7; 34 -5.3; 37 -5.6; 41 -5.7; 45 -5.8; 49 -5.9; 54 -5.9; 60 -5.9; 66 -5.9; 72 -5.9; 79 -6.1; 87 -6.4; 96 -6.7; 106 -6.8; 116 -6.7; 128 -7.0; 141 -7.0; 155 -7.2; 170 -7.1; 187 -7.1; 206 -7.0; 227 -6.8; 249 -6.8; 274 -6.7; 302 -6.4; 332 -6.3; 365 -6.3; 402 -5.8; 442 -5.1; 486 -5.0; 535 -4.4; 588 -4.2; 647 -4.8; 712 -5.8; 783 -7.4; 861 -7.0; 947 -4.7; 1042 -5.9; 1146 -6.3; 1261 -6.6; 1387 -7.1; 1526 -7.6; 1678 -8.3; 1846 -8.3; 2031 -8.4; 2234 -8.7; 2457 -8.5; 2703 -6.6; 2973 -7.3; 3270 -8.4; 3597 -9.2; 3957 -10.0; 4353 -11.1; 4788 -11.1; 5267 -11.8; 5793 -9.6; 6373 -8.2; 7010 -10.7; 7711 -11.3; 8482 -10.1; 9330 -7.2; 10263 -5.9; 11289 -8.3; 12418 -10.8; 13660 -10.6; 15026 -7.9; 16529 -6.6; 18182 -7.2; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 JMoney Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.54 | 5.7 dB  |
| Peaking | 1784 Hz  | 1.82 | -2.3 dB |
| Peaking | 5353 Hz  | 0.83 | -5.5 dB |
| Peaking | 13224 Hz | 2.66 | -5.4 dB |
| Peaking | 17939 Hz | 2.27 | -1.8 dB |
| Peaking | 153 Hz   | 0.77 | -1.9 dB |
| Peaking | 2853 Hz  | 7.01 | 1.9 dB  |
| Peaking | 6251 Hz  | 4.69 | 5.2 dB  |
| Peaking | 7714 Hz  | 1.15 | -3.7 dB |
| Peaking | 9883 Hz  | 3.39 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20JMoney%20Pads/Denon%20AH-D5000%20JMoney%20Pads.png)