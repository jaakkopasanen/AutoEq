# Bowers & Wilkins P7 Wireless Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.5; 28 -3.0; 31 -3.4; 34 -3.7; 37 -3.9; 41 -4.2; 45 -4.4; 49 -4.5; 54 -4.7; 60 -4.8; 66 -5.0; 72 -5.2; 79 -5.5; 87 -5.6; 96 -5.9; 106 -6.0; 116 -6.0; 128 -6.0; 141 -6.0; 155 -6.1; 170 -6.0; 187 -5.5; 206 -5.4; 227 -5.2; 249 -5.1; 274 -4.8; 302 -4.8; 332 -4.5; 365 -4.3; 402 -4.3; 442 -4.4; 486 -4.6; 535 -4.5; 588 -4.3; 647 -4.6; 712 -5.1; 783 -5.3; 861 -5.8; 947 -6.1; 1042 -6.0; 1146 -6.4; 1261 -7.4; 1387 -8.4; 1526 -9.4; 1678 -10.0; 1846 -10.2; 2031 -9.7; 2234 -9.6; 2457 -8.8; 2703 -7.3; 2973 -3.4; 3270 -0.5; 3597 -3.3; 3957 -5.3; 4353 -5.5; 4788 -5.0; 5267 -3.6; 5793 -5.5; 6373 -2.4; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.52 | 5.2 dB  |
| Peaking | 500 Hz  | 0.67 | 2.1 dB  |
| Peaking | 1948 Hz | 1.29 | -4.8 dB |
| Peaking | 3249 Hz | 4.32 | 7.5 dB  |
| Peaking | 6568 Hz | 5.11 | 4.2 dB  |
| Peaking | 115 Hz  | 0.6  | 1.1 dB  |
| Peaking | 125 Hz  | 0.99 | -1.5 dB |
| Peaking | 5375 Hz | 3.41 | 3.1 dB  |
| Peaking | 5719 Hz | 0.79 | -0.6 dB |
| Peaking | 5968 Hz | 8.92 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive.png)