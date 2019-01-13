# Beyerdynamic DT 48 Loose
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.5; 79 4.6; 87 3.8; 96 4.1; 106 2.0; 116 0.9; 128 -0.6; 141 -1.5; 155 -2.4; 170 -3.1; 187 -4.4; 206 -4.9; 227 -4.6; 249 -4.3; 274 -3.9; 302 -3.6; 332 -2.5; 365 -1.9; 402 -0.7; 442 0.8; 486 1.7; 535 2.8; 588 4.3; 647 4.1; 712 3.1; 783 2.8; 861 1.7; 947 0.9; 1042 -0.8; 1146 -2.8; 1261 -4.2; 1387 -5.0; 1526 -6.1; 1678 -7.2; 1846 -7.4; 2031 -7.3; 2234 -6.1; 2457 -3.2; 2703 -0.4; 2973 0.7; 3270 1.0; 3597 2.1; 3957 3.5; 4353 3.4; 4788 5.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -3.2; 8482 -7.4; 9330 -5.0; 10263 -1.1; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -5.9; 16529 -9.3; 18182 -8.1; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 Loose GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 Loose ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.85 | 7.3 dB   |
| Peaking | 1887 Hz  | 1.76 | -10.0 dB |
| Peaking | 7133 Hz  | 0.68 | 11.7 dB  |
| Peaking | 8465 Hz  | 2.44 | -17.9 dB |
| Peaking | 17082 Hz | 1.31 | -11.4 dB |
| Peaking | 40 Hz    | 1.06 | -8.3 dB  |
| Peaking | 54 Hz    | 0.31 | 8.0 dB   |
| Peaking | 204 Hz   | 0.65 | -8.8 dB  |
| Peaking | 620 Hz   | 1.21 | 6.2 dB   |
| Peaking | 1265 Hz  | 3.06 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20Loose/Beyerdynamic%20DT%2048%20Loose.png)