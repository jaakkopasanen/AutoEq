# Bowers & Wilkins P7 Wireless Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.5; 28 -3.0; 31 -3.4; 34 -3.7; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.7; 60 -4.9; 66 -5.0; 72 -5.3; 79 -5.5; 87 -5.7; 96 -6.0; 106 -6.0; 116 -6.0; 128 -6.1; 141 -6.0; 155 -6.1; 170 -6.0; 187 -5.5; 206 -5.4; 227 -5.3; 249 -5.1; 274 -4.9; 302 -4.8; 332 -4.6; 365 -4.4; 402 -4.4; 442 -4.5; 486 -4.6; 535 -4.6; 588 -4.4; 647 -4.7; 712 -5.2; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.1; 1146 -6.5; 1261 -7.4; 1387 -8.5; 1526 -9.4; 1678 -10.1; 1846 -10.2; 2031 -9.7; 2234 -9.6; 2457 -8.8; 2703 -7.4; 2973 -3.4; 3270 -0.5; 3597 -3.3; 3957 -5.4; 4353 -5.5; 4788 -5.0; 5267 -3.6; 5793 -5.5; 6373 -2.4; 7010 -2.9; 7711 -5.1; 8482 -5.3; 9330 -5.7; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.32 | 3.6 dB  |
| Peaking | 526 Hz  | 1.16 | 1.3 dB  |
| Peaking | 1948 Hz | 1.22 | -5.4 dB |
| Peaking | 3231 Hz | 5.1  | 7.3 dB  |
| Peaking | 6625 Hz | 7.53 | 4.6 dB  |
| Peaking | 126 Hz  | 1.66 | -1.0 dB |
| Peaking | 1120 Hz | 6.55 | 0.6 dB  |
| Peaking | 1486 Hz | 6.06 | -0.5 dB |
| Peaking | 5324 Hz | 7.58 | 2.0 dB  |
| Peaking | 5981 Hz | 9.85 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive/Bowers%20&%20Wilkins%20P7%20Wireless%20Wired%20Passive.png)