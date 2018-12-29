# Read and Heath Acoustics MA-350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -10.3; 23 -10.2; 25 -10.2; 28 -10.1; 31 -9.9; 34 -9.8; 37 -9.7; 41 -9.6; 45 -9.5; 49 -9.4; 54 -9.2; 60 -9.1; 66 -9.1; 72 -8.9; 79 -8.9; 87 -8.9; 96 -8.8; 106 -8.6; 116 -8.3; 128 -8.0; 141 -7.7; 155 -7.5; 170 -7.0; 187 -6.5; 206 -6.1; 227 -5.5; 249 -5.0; 274 -4.4; 302 -3.8; 332 -3.2; 365 -2.5; 402 -2.0; 442 -1.3; 486 -1.1; 535 -0.7; 588 -0.2; 647 -0.1; 712 -0.0; 783 0.2; 861 -0.0; 947 -0.0; 1042 -0.0; 1146 -0.1; 1261 -0.0; 1387 -0.2; 1526 -0.4; 1678 -0.3; 1846 0.3; 2031 1.0; 2234 1.6; 2457 2.1; 2703 2.5; 2973 2.4; 3270 1.8; 3597 0.8; 3957 -1.1; 4353 -4.2; 4788 -7.6; 5267 -8.9; 5793 -3.6; 6373 1.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read and Heath Acoustics MA-350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read and Heath Acoustics MA-350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.19 | -9.9 dB  |
| Peaking | 159 Hz  | 0.72 | -3.8 dB  |
| Peaking | 3053 Hz | 1.57 | 3.8 dB   |
| Peaking | 5131 Hz | 2.56 | -11.3 dB |
| Peaking | 6528 Hz | 3.82 | 6.5 dB   |
| Peaking | 293 Hz  | 2.77 | -0.5 dB  |
| Peaking | 654 Hz  | 1.3  | 0.7 dB   |
| Peaking | 1589 Hz | 4.39 | -0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20and%20Heath%20Acoustics%20MA-350/Read%20and%20Heath%20Acoustics%20MA-350.png)