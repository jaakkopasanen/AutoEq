# Aiaiai TMA-1 Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.4; 28 -2.6; 31 -3.8; 34 -4.9; 37 -5.8; 41 -6.8; 45 -7.6; 49 -8.3; 54 -8.9; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.5; 87 -10.6; 96 -10.8; 106 -10.6; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.4; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.9; 249 -10.8; 274 -10.4; 302 -9.8; 332 -9.6; 365 -9.9; 402 -9.6; 442 -9.4; 486 -9.2; 535 -8.7; 588 -7.8; 647 -6.9; 712 -6.3; 783 -6.1; 861 -6.8; 947 -7.7; 1042 -8.0; 1146 -7.8; 1261 -6.8; 1387 -6.7; 1526 -6.2; 1678 -5.4; 1846 -4.3; 2031 -3.3; 2234 -2.3; 2457 -1.3; 2703 -0.8; 2973 -1.0; 3270 -1.9; 3597 -2.6; 3957 -2.8; 4353 -1.7; 4788 -0.5; 5267 -0.5; 5793 -1.8; 6373 -2.1; 7010 -6.7; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aiaiai TMA-1 Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.02 | 6.8 dB  |
| Peaking | 62 Hz   | 0.74 | -2.7 dB |
| Peaking | 200 Hz  | 0.47 | -4.1 dB |
| Peaking | 2688 Hz | 1.83 | 5.7 dB  |
| Peaking | 5114 Hz | 2.57 | 5.9 dB  |
| Peaking | 526 Hz  | 1.73 | -2.1 dB |
| Peaking | 774 Hz  | 1.03 | 3.5 dB  |
| Peaking | 1017 Hz | 1.86 | -3.5 dB |
| Peaking | 6250 Hz | 8.39 | 3.4 dB  |
| Peaking | 7259 Hz | 3.74 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1%20Studio/Aiaiai%20TMA-1%20Studio.png)