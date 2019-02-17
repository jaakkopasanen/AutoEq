# Noontec Zoro II HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -7.9; 37 -7.9; 41 -8.0; 45 -7.9; 49 -7.9; 54 -8.0; 60 -8.3; 66 -8.4; 72 -8.5; 79 -8.7; 87 -8.7; 96 -9.2; 106 -9.5; 116 -9.3; 128 -9.1; 141 -9.8; 155 -10.4; 170 -10.0; 187 -10.4; 206 -10.3; 227 -10.0; 249 -9.6; 274 -9.0; 302 -8.5; 332 -8.4; 365 -8.2; 402 -8.0; 442 -7.8; 486 -7.8; 535 -7.1; 588 -6.7; 647 -6.4; 712 -6.4; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -7.0; 1387 -7.6; 1526 -8.2; 1678 -8.4; 1846 -8.1; 2031 -7.2; 2234 -6.4; 2457 -5.1; 2703 -4.6; 2973 -3.7; 3270 -3.1; 3597 -1.3; 3957 -0.5; 4353 -0.7; 4788 -2.9; 5267 -3.3; 5793 -2.4; 6373 -3.7; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.36 | -1.5 dB |
| Peaking | 193 Hz  | 0.94 | -3.1 dB |
| Peaking | 1697 Hz | 3.02 | -2.5 dB |
| Peaking | 3935 Hz | 1.95 | 6.1 dB  |
| Peaking | 5961 Hz | 4.8  | 2.6 dB  |
| Peaking | 104 Hz  | 7.22 | -0.5 dB |
| Peaking | 460 Hz  | 3.8  | -0.6 dB |
| Peaking | 738 Hz  | 2.16 | 0.8 dB  |
| Peaking | 6985 Hz | 6.57 | 1.1 dB  |
| Peaking | 7875 Hz | 2.16 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20HD/Noontec%20Zoro%20II%20HD.png)