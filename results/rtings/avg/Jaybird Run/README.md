# Jaybird Run
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.4; 28 -3.4; 31 -3.4; 34 -3.4; 37 -3.4; 41 -3.4; 45 -3.4; 49 -3.4; 54 -3.5; 60 -3.9; 66 -4.2; 72 -4.4; 79 -4.7; 87 -5.1; 96 -5.4; 106 -5.8; 116 -6.2; 128 -6.5; 141 -6.9; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.4; 227 -7.1; 249 -6.6; 274 -6.2; 302 -5.7; 332 -5.2; 365 -4.7; 402 -4.2; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.8; 647 -1.1; 712 -0.6; 783 -0.5; 861 -0.9; 947 -1.6; 1042 -2.5; 1146 -3.3; 1261 -4.0; 1387 -4.2; 1526 -4.6; 1678 -5.1; 1846 -5.8; 2031 -6.5; 2234 -6.8; 2457 -6.7; 2703 -5.8; 2973 -4.4; 3270 -3.0; 3597 -2.0; 3957 -1.4; 4353 -1.1; 4788 -0.8; 5267 -1.2; 5793 -2.9; 6373 -7.7; 7010 -11.9; 7711 -7.9; 8482 -4.5; 9330 -6.3; 10263 -7.2; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 188 Hz   | 1.23 | -3.4 dB |
| Peaking | 740 Hz   | 1.35 | 4.4 dB  |
| Peaking | 2271 Hz  | 1.86 | -3.4 dB |
| Peaking | 4760 Hz  | 1.36 | 5.2 dB  |
| Peaking | 6990 Hz  | 4.13 | -9.7 dB |
| Peaking | 34 Hz    | 0.91 | 1.5 dB  |
| Peaking | 1254 Hz  | 6.13 | -0.3 dB |
| Peaking | 8535 Hz  | 6.09 | 2.0 dB  |
| Peaking | 10028 Hz | 4.33 | -3.5 dB |
| Peaking | 10932 Hz | 4.3  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Run/Jaybird%20Run.png)