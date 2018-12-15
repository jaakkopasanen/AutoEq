# Beyerdynamic Xelento

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.9; 28 2.0; 31 2.0; 34 2.0; 37 2.0; 41 1.9; 45 1.8; 49 1.6; 54 1.3; 60 0.9; 66 0.5; 72 0.1; 79 -0.4; 87 -0.7; 96 -1.4; 106 -1.8; 116 -2.4; 128 -2.8; 141 -3.1; 155 -3.4; 170 -4.4; 187 -5.1; 206 -4.9; 227 -4.7; 249 -4.4; 274 -3.9; 302 -3.3; 332 -2.8; 365 -2.5; 402 -2.2; 442 -1.8; 486 -1.3; 535 -0.9; 588 -0.7; 647 -0.4; 712 -0.0; 783 0.3; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -0.5; 1526 -0.1; 1678 0.4; 1846 1.0; 2031 1.8; 2234 2.7; 2457 3.3; 2703 4.0; 2973 4.6; 3270 5.0; 3597 5.0; 3957 4.2; 4353 2.8; 4788 0.0; 5267 -2.1; 5793 3.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -3.2; 10263 -3.2; 11289 -1.8; 12418 -1.1; 13660 -2.6; 15026 -6.1; 16529 -7.1; 18182 -3.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 213 Hz   | 1.01 | -5.1 dB |
| Peaking | 3157 Hz  | 1.85 | 5.5 dB  |
| Peaking | 6373 Hz  | 7.11 | 6.1 dB  |
| Peaking | 9733 Hz  | 4.17 | -3.5 dB |
| Peaking | 16196 Hz | 1.86 | -7.8 dB |
| Peaking | 34 Hz    | 1.02 | 2.5 dB  |
| Peaking | 823 Hz   | 4.02 | 0.8 dB  |
| Peaking | 1332 Hz  | 3.84 | -1.1 dB |
| Peaking | 5139 Hz  | 2    | 2.7 dB  |
| Peaking | 5161 Hz  | 5.67 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)