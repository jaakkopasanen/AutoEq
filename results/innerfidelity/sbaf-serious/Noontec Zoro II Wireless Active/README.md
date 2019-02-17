# Noontec Zoro II Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.3; 28 -6.8; 31 -7.2; 34 -7.5; 37 -7.8; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.7; 60 -8.9; 66 -9.0; 72 -9.2; 79 -9.7; 87 -10.3; 96 -10.7; 106 -11.1; 116 -11.4; 128 -11.7; 141 -12.0; 155 -12.2; 170 -12.0; 187 -12.2; 206 -12.1; 227 -11.8; 249 -11.5; 274 -10.9; 302 -10.3; 332 -10.1; 365 -9.6; 402 -9.5; 442 -9.3; 486 -8.9; 535 -8.4; 588 -7.5; 647 -6.9; 712 -6.4; 783 -5.8; 861 -5.6; 947 -5.5; 1042 -5.5; 1146 -5.5; 1261 -6.1; 1387 -6.7; 1526 -7.2; 1678 -7.4; 1846 -7.1; 2031 -6.4; 2234 -5.4; 2457 -4.5; 2703 -3.9; 2973 -3.5; 3270 -3.7; 3597 -3.1; 3957 -0.5; 4353 -1.2; 4788 -2.6; 5267 -4.1; 5793 -3.3; 6373 -5.3; 7010 -5.3; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 96 Hz   | 0.41 | -2.8 dB |
| Peaking | 207 Hz  | 0.59 | -4.7 dB |
| Peaking | 1705 Hz | 4.17 | -2.2 dB |
| Peaking | 4110 Hz | 2.15 | 4.7 dB  |
| Peaking | 71 Hz   | 4.92 | 0.5 dB  |
| Peaking | 482 Hz  | 3.33 | -1.0 dB |
| Peaking | 875 Hz  | 1.84 | 1.1 dB  |
| Peaking | 2567 Hz | 1.11 | -0.9 dB |
| Peaking | 2642 Hz | 3.37 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Active/Noontec%20Zoro%20II%20Wireless%20Active.png)