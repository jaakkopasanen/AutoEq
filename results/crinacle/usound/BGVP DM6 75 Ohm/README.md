# BGVP DM6 75 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.0; 37 -1.4; 41 -1.9; 45 -2.4; 49 -2.8; 54 -3.3; 60 -3.7; 66 -4.2; 72 -4.6; 79 -5.0; 87 -5.6; 96 -6.1; 106 -6.6; 116 -7.2; 128 -7.5; 141 -7.9; 155 -8.1; 170 -8.4; 187 -8.7; 206 -8.9; 227 -9.0; 249 -9.0; 274 -9.1; 302 -9.2; 332 -9.2; 365 -9.1; 402 -9.1; 442 -9.1; 486 -9.0; 535 -8.9; 588 -8.8; 647 -8.6; 712 -8.4; 783 -8.1; 861 -7.9; 947 -7.9; 1042 -8.2; 1146 -8.9; 1261 -9.7; 1387 -9.9; 1526 -9.5; 1678 -8.4; 1846 -7.0; 2031 -5.5; 2234 -4.3; 2457 -3.1; 2703 -2.1; 2973 -1.5; 3270 -1.4; 3597 -1.9; 3957 -3.2; 4353 -5.7; 4788 -5.3; 5267 -2.3; 5793 -1.9; 6373 -4.9; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 75 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 75 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.38 | 6.2 dB  |
| Peaking | 264 Hz  | 0.36 | -3.0 dB |
| Peaking | 1424 Hz | 2.41 | -3.6 dB |
| Peaking | 2989 Hz | 1.73 | 5.7 dB  |
| Peaking | 5647 Hz | 5.99 | 4.5 dB  |
| Peaking | 3732 Hz | 6.57 | 1.0 dB  |
| Peaking | 4470 Hz | 9.91 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DM6%2075%20Ohm/BGVP%20DM6%2075%20Ohm.png)