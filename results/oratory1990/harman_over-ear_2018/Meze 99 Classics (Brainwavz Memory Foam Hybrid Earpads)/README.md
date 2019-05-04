# Meze 99 Classics (Brainwavz Memory Foam Hybrid Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.9; 25 -7.3; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.7; 41 -8.9; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.4; 72 -9.3; 79 -9.3; 87 -9.2; 96 -9.1; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.3; 155 -8.1; 170 -7.6; 187 -6.9; 206 -6.0; 227 -4.9; 249 -3.5; 274 -1.7; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -1.4; 486 -3.1; 535 -4.3; 588 -5.0; 647 -5.4; 712 -5.5; 783 -5.6; 861 -5.7; 947 -5.7; 1042 -5.8; 1146 -6.5; 1261 -6.3; 1387 -6.2; 1526 -6.2; 1678 -6.4; 1846 -6.6; 2031 -7.0; 2234 -7.6; 2457 -8.3; 2703 -8.8; 2973 -8.6; 3270 -7.5; 3597 -4.6; 3957 -2.4; 4353 -7.9; 4788 -11.1; 5267 -13.2; 5793 -14.6; 6373 -13.7; 7010 -12.0; 7711 -12.7; 8482 -10.7; 9330 -6.7; 10263 -6.6; 11289 -9.1; 12418 -10.7; 13660 -11.5; 15026 -12.4; 16529 -13.6; 18182 -12.6; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics (Brainwavz Memory Foam Hybrid Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics (Brainwavz Memory Foam Hybrid Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 122 Hz   | 0.29 | -3.5 dB |
| Peaking | 336 Hz   | 1.14 | 9.0 dB  |
| Peaking | 3939 Hz  | 5.68 | 8.6 dB  |
| Peaking | 5678 Hz  | 1.34 | -7.9 dB |
| Peaking | 16845 Hz | 0.9  | -7.6 dB |
| Peaking | 16 Hz    | 2.1  | 1.2 dB  |
| Peaking | 8093 Hz  | 5.36 | -3.2 dB |
| Peaking | 8774 Hz  | 1.88 | -0.3 dB |
| Peaking | 9681 Hz  | 2.55 | 4.2 dB  |
| Peaking | 12477 Hz | 2.23 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%2099%20Classics%20(Brainwavz%20Memory%20Foam%20Hybrid%20Earpads)/Meze%2099%20Classics%20(Brainwavz%20Memory%20Foam%20Hybrid%20Earpads).png)