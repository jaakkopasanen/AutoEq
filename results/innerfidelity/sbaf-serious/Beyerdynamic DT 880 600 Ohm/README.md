# Beyerdynamic DT 880 600 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 4.0; 37 3.7; 41 3.3; 45 3.0; 49 2.7; 54 2.2; 60 1.7; 66 1.5; 72 1.9; 79 1.3; 87 0.2; 96 -0.5; 106 -0.9; 116 -1.2; 128 -1.6; 141 -1.9; 155 -2.2; 170 -2.3; 187 -2.4; 206 -2.6; 227 -2.5; 249 -2.5; 274 -2.4; 302 -2.2; 332 -2.2; 365 -2.0; 402 -1.9; 442 -1.3; 486 -1.2; 535 -1.3; 588 -1.0; 647 -0.8; 712 -0.7; 783 -0.3; 861 -0.4; 947 -0.2; 1042 0.2; 1146 0.5; 1261 0.7; 1387 0.4; 1526 -0.0; 1678 -0.6; 1846 -1.0; 2031 -0.7; 2234 -0.4; 2457 0.5; 2703 0.1; 2973 0.4; 3270 0.7; 3597 1.1; 3957 1.0; 4353 0.3; 4788 1.1; 5267 0.9; 5793 -1.8; 6373 -1.3; 7010 -1.4; 7711 -3.5; 8482 -6.5; 9330 -6.7; 10263 -1.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.44 | 6.2 dB  |
| Peaking | 75 Hz    | 3.93 | 1.2 dB  |
| Peaking | 205 Hz   | 0.57 | -2.9 dB |
| Peaking | 3916 Hz  | 2.29 | 1.3 dB  |
| Peaking | 8803 Hz  | 3.61 | -7.8 dB |
| Peaking | 1250 Hz  | 3.08 | 1.0 dB  |
| Peaking | 1839 Hz  | 4.24 | -1.2 dB |
| Peaking | 5106 Hz  | 9.01 | 1.8 dB  |
| Peaking | 5881 Hz  | 7.09 | -1.9 dB |
| Peaking | 11115 Hz | 6.54 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20600%20Ohm/Beyerdynamic%20DT%20880%20600%20Ohm.png)