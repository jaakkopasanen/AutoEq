# Noontec Zoro II Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.2; 25 -5.7; 28 -6.2; 31 -6.6; 34 -7.0; 37 -7.2; 41 -7.5; 45 -7.8; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.4; 72 -8.6; 79 -9.1; 87 -9.8; 96 -10.2; 106 -10.6; 116 -10.9; 128 -11.1; 141 -11.5; 155 -11.6; 170 -11.4; 187 -11.6; 206 -11.5; 227 -11.3; 249 -11.0; 274 -10.3; 302 -9.8; 332 -9.6; 365 -9.1; 402 -9.0; 442 -8.7; 486 -8.4; 535 -7.8; 588 -6.9; 647 -6.3; 712 -5.9; 783 -5.2; 861 -5.0; 947 -5.0; 1042 -5.0; 1146 -4.9; 1261 -5.5; 1387 -6.2; 1526 -6.6; 1678 -6.9; 1846 -6.6; 2031 -5.8; 2234 -4.9; 2457 -4.0; 2703 -3.4; 2973 -2.9; 3270 -3.2; 3597 -2.6; 3957 -0.5; 4353 -0.7; 4788 -2.0; 5267 -3.6; 5793 -2.7; 6373 -4.8; 7010 -4.8; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.89 | 2.2 dB  |
| Peaking | 163 Hz  | 0.98 | -1.1 dB |
| Peaking | 176 Hz  | 0.44 | -4.2 dB |
| Peaking | 859 Hz  | 1.75 | 2.4 dB  |
| Peaking | 4103 Hz | 1.45 | 5.7 dB  |
| Peaking | 1174 Hz | 5.26 | 0.9 dB  |
| Peaking | 1781 Hz | 1.87 | -2.0 dB |
| Peaking | 2600 Hz | 1.22 | 1.8 dB  |
| Peaking | 3440 Hz | 5.35 | -2.0 dB |
| Peaking | 8741 Hz | 2.55 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Active/Noontec%20Zoro%20II%20Wireless%20Active.png)