# Sendy Aiya
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.4; 25 -14.5; 28 -14.5; 31 -14.5; 34 -14.5; 37 -14.4; 41 -14.3; 45 -14.2; 49 -14.1; 54 -13.9; 60 -13.8; 66 -13.7; 72 -13.5; 79 -13.4; 87 -13.3; 96 -13.2; 106 -13.1; 116 -12.9; 128 -12.7; 141 -12.4; 155 -12.1; 170 -11.6; 187 -11.2; 206 -10.7; 227 -10.2; 249 -9.6; 274 -9.0; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.6; 442 -5.9; 486 -5.3; 535 -4.7; 588 -4.1; 647 -3.4; 712 -2.9; 783 -2.3; 861 -2.1; 947 -2.2; 1042 -2.6; 1146 -3.2; 1261 -3.9; 1387 -4.4; 1526 -4.4; 1678 -4.3; 1846 -4.5; 2031 -5.1; 2234 -6.1; 2457 -7.4; 2703 -8.4; 2973 -8.6; 3270 -8.8; 3597 -10.5; 3957 -11.3; 4353 -12.4; 4788 -6.6; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sendy Aiya GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sendy Aiya ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.09 | -7.8 dB  |
| Peaking | 769 Hz  | 0.44 | 4.0 dB   |
| Peaking | 848 Hz  | 1.99 | 1.7 dB   |
| Peaking | 4328 Hz | 1.53 | -10.8 dB |
| Peaking | 5513 Hz | 2.29 | 12.7 dB  |
| Peaking | 2041 Hz | 2.64 | 2.0 dB   |
| Peaking | 2570 Hz | 1.35 | -2.1 dB  |
| Peaking | 3292 Hz | 3.01 | 1.8 dB   |
| Peaking | 6590 Hz | 7.07 | 2.4 dB   |
| Peaking | 7588 Hz | 2.55 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sendy%20Aiya/Sendy%20Aiya.png)