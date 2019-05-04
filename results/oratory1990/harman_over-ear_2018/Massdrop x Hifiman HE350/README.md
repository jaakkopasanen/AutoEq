# Massdrop x Hifiman HE350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.5; 41 -2.1; 45 -2.7; 49 -3.1; 54 -3.6; 60 -4.1; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -6.0; 106 -5.9; 116 -6.3; 128 -7.0; 141 -7.3; 155 -7.4; 170 -7.3; 187 -7.2; 206 -7.2; 227 -7.2; 249 -7.0; 274 -6.7; 302 -6.3; 332 -6.1; 365 -5.9; 402 -6.0; 442 -6.1; 486 -6.3; 535 -6.5; 588 -6.8; 647 -6.9; 712 -7.1; 783 -7.1; 861 -6.7; 947 -7.0; 1042 -6.9; 1146 -6.6; 1261 -6.2; 1387 -5.7; 1526 -5.1; 1678 -3.9; 1846 -2.8; 2031 -1.5; 2234 -1.3; 2457 -2.2; 2703 -3.0; 2973 -3.8; 3270 -5.1; 3597 -6.7; 3957 -8.7; 4353 -10.8; 4788 -12.8; 5267 -14.1; 5793 -13.0; 6373 -10.2; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -11.0; 11289 -13.4; 12418 -13.4; 13660 -11.9; 15026 -10.7; 16529 -10.3; 18182 -10.6; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman HE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman HE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.6  | 6.2 dB  |
| Peaking | 158 Hz   | 1.5  | -1.4 dB |
| Peaking | 2272 Hz  | 1.87 | 5.8 dB  |
| Peaking | 5104 Hz  | 3.27 | -7.8 dB |
| Peaking | 17331 Hz | 0.31 | -5.4 dB |
| Peaking | 949 Hz   | 1.94 | -0.9 dB |
| Peaking | 5962 Hz  | 4.43 | -3.2 dB |
| Peaking | 7938 Hz  | 1.66 | 4.3 dB  |
| Peaking | 11553 Hz | 2.07 | -4.9 dB |
| Peaking | 16564 Hz | 1.49 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20HE350/Massdrop%20x%20Hifiman%20HE350.png)