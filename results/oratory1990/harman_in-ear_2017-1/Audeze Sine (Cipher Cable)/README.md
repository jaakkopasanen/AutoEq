# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.8; 25 -4.7; 28 -4.7; 31 -4.7; 34 -4.7; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.2; 54 -5.3; 60 -5.6; 66 -6.1; 72 -6.4; 79 -6.6; 87 -6.8; 96 -7.3; 106 -7.6; 116 -7.7; 128 -7.8; 141 -7.8; 155 -7.8; 170 -7.6; 187 -7.2; 206 -6.5; 227 -6.6; 249 -7.0; 274 -7.2; 302 -7.0; 332 -6.9; 365 -6.8; 402 -6.7; 442 -6.9; 486 -7.1; 535 -6.9; 588 -6.8; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.8; 1042 -7.1; 1146 -7.4; 1261 -7.6; 1387 -7.6; 1526 -7.3; 1678 -7.1; 1846 -7.4; 2031 -7.6; 2234 -7.1; 2457 -6.2; 2703 -6.2; 2973 -6.5; 3270 -6.7; 3597 -6.7; 3957 -5.2; 4353 -3.0; 4788 -2.0; 5267 -2.0; 5793 -1.4; 6373 -0.5; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -6.0; 10263 -10.0; 11289 -11.5; 12418 -12.5; 13660 -17.4; 15026 -24.0; 16529 -29.0; 18182 -29.7; 20000 -24.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.53 | 3.1 dB   |
| Peaking | 94 Hz    | 0.49 | -3.3 dB  |
| Peaking | 2845 Hz  | 0.43 | -8.2 dB  |
| Peaking | 6314 Hz  | 0.38 | 18.0 dB  |
| Peaking | 17441 Hz | 0.33 | -28.9 dB |
| Peaking | 2525 Hz  | 5.96 | 1.1 dB   |
| Peaking | 3576 Hz  | 5.52 | -1.8 dB  |
| Peaking | 6748 Hz  | 2.05 | 2.2 dB   |
| Peaking | 7494 Hz  | 4.51 | -3.8 dB  |
| Peaking | 12540 Hz | 6.52 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -32.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)