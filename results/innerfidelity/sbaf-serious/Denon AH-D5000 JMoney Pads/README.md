# Denon AH-D5000 JMoney Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.7; 28 -2.8; 31 -3.6; 34 -4.1; 37 -4.4; 41 -4.6; 45 -4.6; 49 -4.7; 54 -4.8; 60 -4.7; 66 -4.7; 72 -4.7; 79 -4.9; 87 -5.2; 96 -5.5; 106 -5.7; 116 -5.6; 128 -5.8; 141 -5.8; 155 -6.0; 170 -6.0; 187 -6.0; 206 -5.8; 227 -5.7; 249 -5.7; 274 -5.5; 302 -5.2; 332 -5.2; 365 -5.2; 402 -4.6; 442 -3.9; 486 -3.8; 535 -3.3; 588 -3.1; 647 -3.6; 712 -4.6; 783 -6.2; 861 -5.9; 947 -3.5; 1042 -4.7; 1146 -5.2; 1261 -5.5; 1387 -5.9; 1526 -6.5; 1678 -7.1; 1846 -7.1; 2031 -7.2; 2234 -7.5; 2457 -7.4; 2703 -5.5; 2973 -6.1; 3270 -7.3; 3597 -8.1; 3957 -8.9; 4353 -9.9; 4788 -9.9; 5267 -10.6; 5793 -8.4; 6373 -7.0; 7010 -9.5; 7711 -10.1; 8482 -8.9; 9330 -6.4; 10263 -6.3; 11289 -7.2; 12418 -9.6; 13660 -9.4; 15026 -6.8; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 JMoney Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 548 Hz   | 1.23 | 2.9 dB  |
| Peaking | 5179 Hz  | 1.15 | -3.5 dB |
| Peaking | 13079 Hz | 3.53 | -3.8 dB |
| Peaking | 22050 Hz | 2.04 | -1.5 dB |
| Peaking | 20 Hz    | 1.22 | 5.9 dB  |
| Peaking | 69 Hz    | 1.38 | 1.2 dB  |
| Peaking | 986 Hz   | 8.82 | 1.8 dB  |
| Peaking | 6231 Hz  | 9.12 | 2.9 dB  |
| Peaking | 7687 Hz  | 5.65 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20JMoney%20Pads/Denon%20AH-D5000%20JMoney%20Pads.png)