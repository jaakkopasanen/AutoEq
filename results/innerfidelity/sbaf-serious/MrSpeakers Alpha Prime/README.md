# MrSpeakers Alpha Prime
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.8; 25 -8.0; 28 -8.1; 31 -8.2; 34 -8.2; 37 -8.3; 41 -8.4; 45 -8.3; 49 -8.3; 54 -8.5; 60 -8.6; 66 -8.5; 72 -8.6; 79 -8.7; 87 -8.9; 96 -8.9; 106 -8.7; 116 -8.5; 128 -8.6; 141 -9.3; 155 -9.1; 170 -8.0; 187 -8.3; 206 -8.6; 227 -8.4; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.7; 365 -8.6; 402 -8.1; 442 -7.8; 486 -8.4; 535 -8.2; 588 -7.8; 647 -6.9; 712 -7.4; 783 -7.9; 861 -8.3; 947 -8.3; 1042 -7.5; 1146 -7.5; 1261 -6.9; 1387 -6.6; 1526 -6.6; 1678 -6.3; 1846 -4.6; 2031 -3.3; 2234 -2.8; 2457 -2.6; 2703 -2.5; 2973 -1.9; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -3.0; 4788 -5.9; 5267 -6.7; 5793 -7.0; 6373 -7.6; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Alpha Prime GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Prime ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.73 | -1.1 dB |
| Peaking | 106 Hz  | 0.52 | -2.0 dB |
| Peaking | 355 Hz  | 0.97 | -1.4 dB |
| Peaking | 947 Hz  | 2.26 | -1.7 dB |
| Peaking | 3180 Hz | 1.5  | 5.8 dB  |
| Peaking | 2174 Hz | 3.5  | 2.5 dB  |
| Peaking | 3956 Hz | 3.5  | 5.5 dB  |
| Peaking | 4187 Hz | 0.89 | -3.2 dB |
| Peaking | 6616 Hz | 3.34 | -1.2 dB |
| Peaking | 7168 Hz | 5.81 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Prime/MrSpeakers%20Alpha%20Prime.png)