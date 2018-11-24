# Beyerdynamic DT 48

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.7; 72 -0.8; 79 -7.3; 87 -6.0; 96 -3.6; 106 -3.6; 116 -3.3; 128 -2.7; 141 -2.1; 155 -1.2; 170 -2.0; 187 -1.8; 206 -1.3; 227 -0.7; 249 -0.1; 274 0.5; 302 1.2; 332 1.7; 365 2.1; 402 2.7; 442 3.8; 486 4.7; 535 5.8; 588 6.0; 647 5.8; 712 4.1; 783 3.4; 861 2.7; 947 1.0; 1042 -0.7; 1146 -2.6; 1261 -3.7; 1387 -4.4; 1526 -5.4; 1678 -6.5; 1846 -6.9; 2031 -6.6; 2234 -5.7; 2457 -2.8; 2703 0.0; 2973 1.9; 3270 2.3; 3597 4.2; 3957 5.4; 4353 5.8; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.4; 7711 -4.7; 8482 -9.6; 9330 -6.4; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -4.1; 16529 -9.2; 18182 -10.2; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.56 | 7.5 dB   |
| Peaking | 1844 Hz  | 1.03 | -18.5 dB |
| Peaking | 4044 Hz  | 0.15 | 11.5 dB  |
| Peaking | 8577 Hz  | 3.15 | -18.1 dB |
| Peaking | 17373 Hz | 0.95 | -15.5 dB |
| Peaking | 66 Hz    | 2.02 | 10.7 dB  |
| Peaking | 79 Hz    | 3.44 | -11.9 dB |
| Peaking | 118 Hz   | 0.63 | -3.6 dB  |
| Peaking | 579 Hz   | 1.88 | 3.9 dB   |
| Peaking | 1169 Hz  | 3.58 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048/Beyerdynamic%20DT%2048.png)