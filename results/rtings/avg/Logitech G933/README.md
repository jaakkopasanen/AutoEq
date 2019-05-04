# Logitech G933
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.6; 25 -7.3; 28 -8.1; 31 -8.6; 34 -8.8; 37 -8.8; 41 -8.6; 45 -8.3; 49 -8.2; 54 -8.4; 60 -8.7; 66 -8.9; 72 -8.9; 79 -8.8; 87 -8.7; 96 -8.3; 106 -7.7; 116 -7.0; 128 -6.7; 141 -6.9; 155 -7.0; 170 -6.8; 187 -6.0; 206 -5.0; 227 -4.0; 249 -2.9; 274 -1.9; 302 -1.1; 332 -0.9; 365 -1.1; 402 -1.3; 442 -1.0; 486 -1.1; 535 -1.5; 588 -1.7; 647 -1.9; 712 -2.0; 783 -1.9; 861 -1.6; 947 -1.6; 1042 -2.0; 1146 -1.6; 1261 -1.8; 1387 -2.1; 1526 -2.5; 1678 -2.4; 1846 -2.0; 2031 -1.7; 2234 -1.8; 2457 -1.7; 2703 -2.6; 2973 -4.8; 3270 -5.7; 3597 -6.3; 3957 -8.0; 4353 -7.1; 4788 -4.9; 5267 -2.7; 5793 -1.6; 6373 -0.5; 7010 -3.0; 7711 -6.4; 8482 -8.8; 9330 -7.8; 10263 -4.9; 11289 -3.6; 12418 -3.7; 13660 -5.3; 15026 -4.9; 16529 -4.1; 18182 -8.0; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G933 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G933 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.5  | -6.4 dB  |
| Peaking | 164 Hz   | 2.57 | -2.8 dB  |
| Peaking | 911 Hz   | 0.1  | 2.4 dB   |
| Peaking | 3849 Hz  | 2.59 | -6.5 dB  |
| Peaking | 8786 Hz  | 3.83 | -7.0 dB  |
| Peaking | 93 Hz    | 4.1  | -0.9 dB  |
| Peaking | 335 Hz   | 2.58 | 1.5 dB   |
| Peaking | 1199 Hz  | 0.76 | -0.6 dB  |
| Peaking | 6210 Hz  | 6.37 | 3.3 dB   |
| Peaking | 19866 Hz | 1.16 | -12.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G933/Logitech%20G933.png)