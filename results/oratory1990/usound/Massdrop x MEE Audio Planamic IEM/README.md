# Massdrop x MEE Audio Planamic IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.6; 31 -9.7; 34 -9.8; 37 -9.9; 41 -10.1; 45 -10.2; 49 -10.3; 54 -10.4; 60 -10.6; 66 -10.8; 72 -11.0; 79 -11.2; 87 -11.4; 96 -11.6; 106 -11.7; 116 -11.7; 128 -11.6; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.0; 206 -10.8; 227 -10.9; 249 -10.6; 274 -10.1; 302 -9.6; 332 -8.9; 365 -8.1; 402 -7.4; 442 -7.1; 486 -6.7; 535 -6.1; 588 -5.6; 647 -5.1; 712 -4.6; 783 -4.2; 861 -3.9; 947 -4.0; 1042 -4.3; 1146 -4.8; 1261 -5.4; 1387 -5.9; 1526 -6.3; 1678 -6.8; 1846 -7.0; 2031 -7.4; 2234 -8.2; 2457 -9.6; 2703 -10.2; 2973 -10.5; 3270 -10.8; 3597 -11.6; 3957 -12.5; 4353 -9.5; 4788 -4.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x MEE Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x MEE Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.47 | -3.6 dB |
| Peaking | 131 Hz  | 1.12 | -3.7 dB |
| Peaking | 244 Hz  | 2.3  | -2.9 dB |
| Peaking | 3870 Hz | 1.72 | -8.7 dB |
| Peaking | 5436 Hz | 2.27 | 10.2 dB |
| Peaking | 333 Hz  | 3.03 | -0.9 dB |
| Peaking | 879 Hz  | 1.39 | 3.0 dB  |
| Peaking | 2541 Hz | 4.91 | -1.8 dB |
| Peaking | 6571 Hz | 6.83 | 2.5 dB  |
| Peaking | 7566 Hz | 2.24 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Massdrop%20x%20MEE%20Audio%20Planamic%20IEM/Massdrop%20x%20MEE%20Audio%20Planamic%20IEM.png)