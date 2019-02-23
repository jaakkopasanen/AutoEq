# Noontec Zoro II Wireless Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.2; 37 -8.2; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.4; 60 -8.5; 66 -8.6; 72 -8.7; 79 -9.0; 87 -9.5; 96 -10.1; 106 -10.6; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.4; 170 -11.3; 187 -11.5; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.4; 302 -10.1; 332 -9.5; 365 -9.1; 402 -9.0; 442 -8.7; 486 -8.3; 535 -8.0; 588 -7.1; 647 -6.6; 712 -6.2; 783 -5.6; 861 -5.6; 947 -5.5; 1042 -5.5; 1146 -5.5; 1261 -6.1; 1387 -6.7; 1526 -7.2; 1678 -7.4; 1846 -7.1; 2031 -6.3; 2234 -5.5; 2457 -4.7; 2703 -4.2; 2973 -3.5; 3270 -3.8; 3597 -2.7; 3957 -0.5; 4353 -1.4; 4788 -3.8; 5267 -4.2; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.6  | -1.3 dB |
| Peaking | 144 Hz  | 0.85 | -4.2 dB |
| Peaking | 272 Hz  | 1.18 | -2.3 dB |
| Peaking | 3921 Hz | 2.17 | 5.4 dB  |
| Peaking | 6206 Hz | 5.37 | 5.4 dB  |
| Peaking | 491 Hz  | 2.67 | -1.1 dB |
| Peaking | 962 Hz  | 1.03 | 1.6 dB  |
| Peaking | 1646 Hz | 2.12 | -1.9 dB |
| Peaking | 2555 Hz | 4.23 | 1.3 dB  |
| Peaking | 8325 Hz | 3.67 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Passive/Noontec%20Zoro%20II%20Wireless%20Passive.png)