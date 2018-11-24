# Beyerdynamic DT 880 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.5; 34 5.1; 37 4.8; 41 4.3; 45 4.0; 49 3.6; 54 3.1; 60 2.7; 66 2.8; 72 2.7; 79 1.8; 87 1.0; 96 0.4; 106 0.0; 116 -0.3; 128 -0.7; 141 -1.0; 155 -1.3; 170 -1.4; 187 -1.5; 206 -1.7; 227 -1.7; 249 -1.7; 274 -1.6; 302 -1.5; 332 -1.6; 365 -1.5; 402 -1.4; 442 -0.8; 486 -0.7; 535 -0.8; 588 -0.5; 647 -0.4; 712 -0.4; 783 -0.1; 861 -0.4; 947 -0.2; 1042 0.1; 1146 0.3; 1261 0.8; 1387 0.6; 1526 0.2; 1678 -0.1; 1846 -0.4; 2031 0.1; 2234 0.8; 2457 1.6; 2703 1.9; 2973 1.8; 3270 0.8; 3597 -0.3; 3957 -0.2; 4353 -0.4; 4788 -0.0; 5267 -1.4; 5793 -2.5; 6373 -2.2; 7010 -2.7; 7711 -5.5; 8482 -7.5; 9330 -6.5; 10263 -2.3; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -0.8; 16529 -0.6; 18182 -2.6; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.57 | 6.1 dB  |
| Peaking | 70 Hz    | 3.25 | 1.2 dB  |
| Peaking | 207 Hz   | 0.62 | -2.0 dB |
| Peaking | 2719 Hz  | 3.57 | 2.4 dB  |
| Peaking | 8509 Hz  | 2.76 | -8.0 dB |
| Peaking | 1299 Hz  | 3.82 | 0.9 dB  |
| Peaking | 1828 Hz  | 6.27 | -0.7 dB |
| Peaking | 5751 Hz  | 7.75 | -1.6 dB |
| Peaking | 11253 Hz | 6.23 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)