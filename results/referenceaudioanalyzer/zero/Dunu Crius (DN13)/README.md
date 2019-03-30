# Dunu Crius (DN13)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.5; 25 -10.6; 28 -10.7; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.9; 49 -11.0; 54 -11.0; 60 -11.0; 66 -11.0; 72 -11.0; 79 -11.0; 87 -11.0; 96 -10.9; 106 -10.7; 116 -10.7; 128 -10.6; 141 -10.4; 155 -10.1; 170 -10.1; 187 -10.9; 206 -11.7; 227 -12.0; 249 -11.7; 274 -11.4; 302 -11.1; 332 -10.9; 365 -10.7; 402 -10.4; 442 -10.2; 486 -10.0; 535 -9.7; 588 -9.5; 647 -9.2; 712 -8.9; 783 -8.6; 861 -8.3; 947 -8.0; 1042 -7.8; 1146 -7.5; 1261 -7.4; 1387 -7.4; 1526 -7.5; 1678 -7.9; 1846 -8.6; 2031 -9.9; 2234 -11.8; 2457 -13.3; 2703 -12.9; 2973 -9.7; 3270 -4.6; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Crius (DN13) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Crius (DN13) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.49 | -3.7 dB  |
| Peaking | 74 Hz   | 0.98 | -2.0 dB  |
| Peaking | 286 Hz  | 0.51 | -4.5 dB  |
| Peaking | 2586 Hz | 2.23 | -11.0 dB |
| Peaking | 4139 Hz | 1.15 | 8.9 dB   |
| Peaking | 164 Hz  | 5.77 | 0.8 dB   |
| Peaking | 214 Hz  | 5.79 | -0.9 dB  |
| Peaking | 4383 Hz | 6.88 | -1.3 dB  |
| Peaking | 6220 Hz | 2.77 | 4.1 dB   |
| Peaking | 7668 Hz | 1.77 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20Crius%20(DN13)/Dunu%20Crius%20(DN13).png)