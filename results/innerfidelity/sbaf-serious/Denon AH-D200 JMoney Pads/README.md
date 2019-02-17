# Denon AH-D200 JMoney Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -1.9; 31 -2.6; 34 -3.0; 37 -3.2; 41 -3.4; 45 -3.4; 49 -3.5; 54 -3.3; 60 -3.1; 66 -3.2; 72 -3.4; 79 -3.7; 87 -4.0; 96 -4.3; 106 -4.5; 116 -4.6; 128 -4.8; 141 -4.9; 155 -5.0; 170 -4.9; 187 -5.0; 206 -4.9; 227 -4.6; 249 -4.6; 274 -4.6; 302 -4.6; 332 -4.6; 365 -4.4; 402 -4.6; 442 -4.6; 486 -5.3; 535 -5.7; 588 -5.9; 647 -6.6; 712 -7.1; 783 -5.2; 861 -6.7; 947 -6.7; 1042 -6.3; 1146 -5.5; 1261 -5.1; 1387 -5.2; 1526 -5.6; 1678 -5.9; 1846 -5.7; 2031 -5.3; 2234 -5.1; 2457 -5.5; 2703 -5.6; 2973 -4.5; 3270 -5.1; 3597 -7.1; 3957 -8.1; 4353 -8.3; 4788 -7.2; 5267 -9.3; 5793 -7.1; 6373 -5.4; 7010 -8.4; 7711 -8.7; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D200 JMoney Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D200 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.06 | 5.7 dB  |
| Peaking | 65 Hz   | 0.93 | 2.6 dB  |
| Peaking | 304 Hz  | 0.74 | 1.8 dB  |
| Peaking | 5040 Hz | 3.25 | -1.6 dB |
| Peaking | 6591 Hz | 3.34 | -1.4 dB |
| Peaking | 676 Hz  | 6.96 | -1.5 dB |
| Peaking | 2933 Hz | 0.93 | 1.8 dB  |
| Peaking | 4007 Hz | 4.05 | -2.7 dB |
| Peaking | 6305 Hz | 9.49 | 3.3 dB  |
| Peaking | 7561 Hz | 4.89 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D200%20JMoney%20Pads/Denon%20AH-D200%20JMoney%20Pads.png)