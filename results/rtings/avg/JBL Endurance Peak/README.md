# JBL Endurance Peak
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.5; 25 -9.5; 28 -9.5; 31 -9.5; 34 -9.5; 37 -9.4; 41 -9.4; 45 -9.3; 49 -9.2; 54 -9.0; 60 -8.7; 66 -8.5; 72 -8.3; 79 -7.9; 87 -7.5; 96 -7.1; 106 -6.7; 116 -6.4; 128 -6.0; 141 -5.4; 155 -4.6; 170 -3.6; 187 -2.7; 206 -1.9; 227 -1.4; 249 -1.2; 274 -1.3; 302 -1.5; 332 -1.6; 365 -1.7; 402 -1.8; 442 -1.7; 486 -1.6; 535 -1.3; 588 -1.2; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.4; 1042 -2.3; 1146 -2.9; 1261 -3.3; 1387 -3.5; 1526 -3.3; 1678 -3.3; 1846 -3.2; 2031 -3.2; 2234 -3.5; 2457 -4.2; 2703 -4.4; 2973 -4.3; 3270 -4.6; 3597 -4.9; 3957 -5.2; 4353 -5.5; 4788 -6.0; 5267 -6.2; 5793 -6.5; 6373 -5.1; 7010 -6.3; 7711 -6.4; 8482 -3.3; 9330 -3.2; 10263 -3.2; 11289 -3.2; 12418 -3.2; 13660 -3.3; 15026 -9.3; 16529 -12.1; 18182 -8.7; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Peak GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Peak ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.36 | -6.8 dB |
| Peaking | 110 Hz   | 0.99 | -2.9 dB |
| Peaking | 239 Hz   | 0.29 | 3.2 dB  |
| Peaking | 5037 Hz  | 1.1  | -3.0 dB |
| Peaking | 16739 Hz | 1.85 | -9.9 dB |
| Peaking | 803 Hz   | 1.74 | 4.0 dB  |
| Peaking | 842 Hz   | 0.9  | -2.7 dB |
| Peaking | 7407 Hz  | 8.5  | -2.9 dB |
| Peaking | 12644 Hz | 0.91 | 1.9 dB  |
| Peaking | 15281 Hz | 4.64 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Endurance%20Peak/JBL%20Endurance%20Peak.png)