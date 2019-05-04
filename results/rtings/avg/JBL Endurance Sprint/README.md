# JBL Endurance Sprint
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.0; 25 -9.0; 28 -9.1; 31 -9.1; 34 -9.2; 37 -9.2; 41 -9.2; 45 -9.2; 49 -9.1; 54 -8.9; 60 -8.7; 66 -8.5; 72 -8.3; 79 -7.9; 87 -7.5; 96 -7.0; 106 -6.4; 116 -5.7; 128 -5.1; 141 -4.4; 155 -3.6; 170 -2.8; 187 -1.9; 206 -1.3; 227 -0.7; 249 -0.5; 274 -0.5; 302 -0.6; 332 -0.8; 365 -0.9; 402 -1.1; 442 -1.2; 486 -1.3; 535 -1.1; 588 -0.9; 647 -0.6; 712 -0.6; 783 -0.5; 861 -0.7; 947 -1.3; 1042 -2.1; 1146 -2.8; 1261 -3.2; 1387 -3.4; 1526 -3.0; 1678 -2.7; 1846 -3.0; 2031 -3.4; 2234 -3.2; 2457 -2.6; 2703 -2.5; 2973 -3.0; 3270 -3.5; 3597 -3.8; 3957 -4.3; 4353 -5.0; 4788 -6.2; 5267 -7.8; 5793 -8.8; 6373 -7.1; 7010 -6.7; 7711 -7.9; 8482 -6.8; 9330 -3.4; 10263 -3.1; 11289 -3.1; 12418 -4.3; 13660 -9.7; 15026 -17.4; 16529 -20.3; 18182 -15.8; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Sprint GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Sprint ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 73 Hz    | 0.21 | -8.1 dB  |
| Peaking | 238 Hz   | 0.43 | 7.9 dB   |
| Peaking | 5606 Hz  | 3.24 | -5.2 dB  |
| Peaking | 7741 Hz  | 6.23 | -3.1 dB  |
| Peaking | 16797 Hz | 1.36 | -19.1 dB |
| Peaking | 822 Hz   | 3.38 | 1.4 dB   |
| Peaking | 1286 Hz  | 3.2  | -1.1 dB  |
| Peaking | 11767 Hz | 2.25 | 4.6 dB   |
| Peaking | 15046 Hz | 3.48 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB   |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -17.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Endurance%20Sprint/JBL%20Endurance%20Sprint.png)