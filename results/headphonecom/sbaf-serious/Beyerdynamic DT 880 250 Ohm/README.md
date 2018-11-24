# Beyerdynamic DT 880 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 5.1; 25 4.7; 28 4.1; 31 3.7; 34 3.4; 37 3.1; 41 2.8; 45 2.8; 49 2.9; 54 2.6; 60 2.3; 66 1.6; 72 1.4; 79 1.3; 87 0.6; 96 0.0; 106 -0.2; 116 -0.4; 128 -0.8; 141 -1.1; 155 -1.2; 170 -1.5; 187 -1.6; 206 -1.7; 227 -1.7; 249 -1.6; 274 -1.6; 302 -1.5; 332 -1.3; 365 -1.1; 402 -1.0; 442 -0.8; 486 -0.3; 535 -0.4; 588 -0.2; 647 -0.2; 712 -0.0; 783 -0.0; 861 -0.1; 947 0.0; 1042 0.1; 1146 0.7; 1261 1.0; 1387 0.7; 1526 0.2; 1678 -0.1; 1846 -0.3; 2031 0.0; 2234 0.3; 2457 0.6; 2703 0.5; 2973 0.0; 3270 -0.8; 3597 -1.4; 3957 -1.5; 4353 0.0; 4788 0.7; 5267 -2.4; 5793 -4.8; 6373 -4.4; 7010 -2.5; 7711 -4.3; 8482 -5.9; 9330 -5.2; 10263 -1.6; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -3.0; 16529 -3.5; 18182 -4.9; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.75 | 5.6 dB  |
| Peaking | 55 Hz    | 1.34 | 1.7 dB  |
| Peaking | 208 Hz   | 0.84 | -1.9 dB |
| Peaking | 7861 Hz  | 1.63 | -5.0 dB |
| Peaking | 19813 Hz | 1.18 | -9.1 dB |
| Peaking | 1262 Hz  | 4.18 | 1.1 dB  |
| Peaking | 5974 Hz  | 4.74 | -5.9 dB |
| Peaking | 6788 Hz  | 1.7  | 4.0 dB  |
| Peaking | 9031 Hz  | 2.59 | -4.2 dB |
| Peaking | 11024 Hz | 2.54 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)