# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -7.9; 23 -7.8; 25 -7.8; 28 -7.7; 31 -7.6; 34 -7.5; 37 -7.4; 41 -7.2; 45 -7.1; 49 -7.0; 54 -6.8; 60 -6.7; 66 -6.6; 72 -6.5; 79 -6.4; 87 -6.2; 96 -6.3; 106 -6.2; 116 -6.1; 128 -6.0; 141 -5.7; 155 -5.5; 170 -5.9; 187 -6.1; 206 -5.5; 227 -4.9; 249 -4.4; 274 -3.9; 302 -3.3; 332 -2.8; 365 -2.5; 402 -2.2; 442 -1.8; 486 -1.3; 535 -0.9; 588 -0.7; 647 -0.4; 712 -0.0; 783 0.3; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -0.5; 1526 -0.1; 1678 0.4; 1846 1.0; 2031 1.8; 2234 2.7; 2457 3.3; 2703 4.0; 2973 4.6; 3270 5.0; 3597 5.0; 3957 4.2; 4353 2.8; 4788 0.0; 5267 -2.1; 5793 3.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -3.2; 10263 -3.2; 11289 -1.8; 12418 -1.1; 13660 -2.6; 15026 -6.1; 16529 -7.1; 18182 -3.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.27 | -6.3 dB |
| Peaking | 203 Hz   | 0.95 | -2.8 dB |
| Peaking | 3233 Hz  | 1.48 | 5.3 dB  |
| Peaking | 16117 Hz | 1.53 | -7.5 dB |
| Peaking | 18 Hz    | 0.84 | -2.9 dB |
| Peaking | 1373 Hz  | 4.76 | -1.1 dB |
| Peaking | 5272 Hz  | 5.56 | -6.3 dB |
| Peaking | 6156 Hz  | 3.77 | 6.7 dB  |
| Peaking | 9597 Hz  | 4.28 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)