# Empire Ears Legend X sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.4; 28 -13.4; 31 -13.3; 34 -13.2; 37 -13.1; 41 -12.9; 45 -12.8; 49 -12.7; 54 -12.6; 60 -12.4; 66 -12.3; 72 -12.2; 79 -12.1; 87 -11.9; 96 -11.9; 106 -11.8; 116 -11.6; 128 -11.4; 141 -11.2; 155 -10.9; 170 -10.5; 187 -10.2; 206 -9.8; 227 -9.3; 249 -8.8; 274 -8.3; 302 -7.8; 332 -7.3; 365 -6.9; 402 -6.4; 442 -6.0; 486 -5.6; 535 -5.2; 588 -4.8; 647 -4.3; 712 -3.9; 783 -3.5; 861 -3.3; 947 -3.6; 1042 -4.4; 1146 -5.4; 1261 -6.6; 1387 -7.4; 1526 -7.9; 1678 -7.9; 1846 -7.8; 2031 -7.5; 2234 -6.9; 2457 -6.0; 2703 -5.0; 2973 -4.1; 3270 -3.2; 3597 -2.0; 3957 -1.7; 4353 -2.2; 4788 -0.5; 5267 -0.7; 5793 -3.0; 6373 -2.6; 7010 -4.5; 7711 -7.7; 8482 -8.6; 9330 -6.5; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -7.3; 15026 -9.9; 16529 -12.5; 18182 -14.2; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Legend X sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Legend X sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.23 | -7.0 dB |
| Peaking | 146 Hz   | 0.84 | -2.7 dB |
| Peaking | 761 Hz   | 2.05 | 3.3 dB  |
| Peaking | 4710 Hz  | 1.78 | 6.0 dB  |
| Peaking | 17960 Hz | 1.01 | -8.5 dB |
| Peaking | 1737 Hz  | 2.35 | -2.5 dB |
| Peaking | 3380 Hz  | 4.49 | 1.7 dB  |
| Peaking | 6555 Hz  | 6.58 | 2.1 dB  |
| Peaking | 8116 Hz  | 4.53 | -3.4 dB |
| Peaking | 12366 Hz | 2.76 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Legend%20X%20sample%202/Empire%20Ears%20Legend%20X%20sample%202.png)