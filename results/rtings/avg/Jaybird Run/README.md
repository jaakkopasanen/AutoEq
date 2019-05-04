# Jaybird Run
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.1; 28 -8.1; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.1; 45 -8.1; 49 -8.1; 54 -8.1; 60 -8.1; 66 -8.2; 72 -8.3; 79 -8.3; 87 -8.4; 96 -8.4; 106 -8.3; 116 -8.2; 128 -8.1; 141 -8.0; 155 -8.1; 170 -8.2; 187 -7.9; 206 -7.4; 227 -6.9; 249 -6.5; 274 -6.0; 302 -5.5; 332 -5.0; 365 -4.5; 402 -4.0; 442 -3.5; 486 -2.9; 535 -2.3; 588 -1.7; 647 -1.1; 712 -0.6; 783 -0.5; 861 -0.9; 947 -1.6; 1042 -2.5; 1146 -3.4; 1261 -4.1; 1387 -4.3; 1526 -4.6; 1678 -5.2; 1846 -6.0; 2031 -6.8; 2234 -7.5; 2457 -7.4; 2703 -6.3; 2973 -4.0; 3270 -2.1; 3597 -1.0; 3957 -0.6; 4353 -0.6; 4788 -1.1; 5267 -1.5; 5793 -2.8; 6373 -7.2; 7010 -11.9; 7711 -8.5; 8482 -4.7; 9330 -4.9; 10263 -6.5; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.2  | -3.8 dB |
| Peaking | 697 Hz   | 0.98 | 4.9 dB  |
| Peaking | 2386 Hz  | 1.5  | -5.8 dB |
| Peaking | 3995 Hz  | 1.02 | 6.2 dB  |
| Peaking | 7034 Hz  | 4.54 | -9.6 dB |
| Peaking | 175 Hz   | 5.22 | -0.7 dB |
| Peaking | 3226 Hz  | 6.9  | 0.3 dB  |
| Peaking | 8533 Hz  | 7.42 | 1.0 dB  |
| Peaking | 10178 Hz | 6.75 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Run/Jaybird%20Run.png)