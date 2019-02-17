# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -3.9; 25 -3.9; 28 -3.9; 31 -4.0; 34 -3.9; 37 -3.8; 41 -3.8; 45 -4.2; 49 -4.4; 54 -4.5; 60 -4.8; 66 -5.3; 72 -5.7; 79 -5.8; 87 -6.0; 96 -6.5; 106 -6.8; 116 -6.9; 128 -7.1; 141 -7.0; 155 -7.0; 170 -6.8; 187 -6.5; 206 -5.7; 227 -5.8; 249 -6.2; 274 -6.4; 302 -6.3; 332 -6.1; 365 -6.0; 402 -5.9; 442 -6.1; 486 -6.3; 535 -6.1; 588 -6.0; 647 -5.8; 712 -5.7; 783 -5.7; 861 -5.8; 947 -6.1; 1042 -6.3; 1146 -6.6; 1261 -6.8; 1387 -6.9; 1526 -6.5; 1678 -6.3; 1846 -6.6; 2031 -6.8; 2234 -6.4; 2457 -5.3; 2703 -5.5; 2973 -5.7; 3270 -5.9; 3597 -6.0; 3957 -4.5; 4353 -2.2; 4788 -1.2; 5267 -1.3; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -9.3; 11289 -10.8; 12418 -11.7; 13660 -16.7; 15026 -23.2; 16529 -28.2; 18182 -28.9; 20000 -23.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.57 | 2.5 dB   |
| Peaking | 119 Hz   | 1.72 | -1.4 dB  |
| Peaking | 5769 Hz  | 0.98 | 11.9 dB  |
| Peaking | 11798 Hz | 0.83 | 10.3 dB  |
| Peaking | 17160 Hz | 0.28 | -26.6 dB |
| Peaking | 747 Hz   | 2.62 | 0.8 dB   |
| Peaking | 2595 Hz  | 4.81 | 1.3 dB   |
| Peaking | 3860 Hz  | 2.16 | -1.7 dB  |
| Peaking | 4409 Hz  | 4.48 | 2.3 dB   |
| Peaking | 9267 Hz  | 9.19 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB   |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -29.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)