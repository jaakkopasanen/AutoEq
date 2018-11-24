# Beyerdynamic DT 990 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.3; 28 0.6; 31 0.0; 34 -0.5; 37 -0.9; 41 -1.3; 45 -1.6; 49 -1.9; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.6; 128 -4.7; 141 -4.8; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.1; 227 -3.7; 249 -3.3; 274 -2.9; 302 -2.5; 332 -2.2; 365 -1.7; 402 -1.5; 442 -1.5; 486 -1.8; 535 -1.5; 588 -1.0; 647 -0.5; 712 -0.1; 783 0.0; 861 0.1; 947 0.1; 1042 0.0; 1146 0.1; 1261 0.0; 1387 -0.1; 1526 -0.3; 1678 -1.0; 1846 -1.8; 2031 -2.2; 2234 -1.8; 2457 -1.3; 2703 -1.8; 2973 -2.2; 3270 -2.0; 3597 -0.6; 3957 1.6; 4353 -2.2; 4788 -3.5; 5267 -2.1; 5793 -2.3; 6373 -5.4; 7010 -3.7; 7711 -2.9; 8482 -6.5; 9330 -7.7; 10263 -4.3; 11289 -3.5; 12418 -6.6; 13660 -8.7; 15026 -7.5; 16529 -5.8; 18182 -7.8; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.86 | 2.8 dB   |
| Peaking | 135 Hz   | 0.55 | -4.9 dB  |
| Peaking | 12816 Hz | 0.13 | -1.0 dB  |
| Peaking | 13509 Hz | 0.47 | -5.5 dB  |
| Peaking | 19894 Hz | 2.07 | -10.0 dB |
| Peaking | 3912 Hz  | 5.7  | 5.9 dB   |
| Peaking | 3966 Hz  | 1.36 | -2.5 dB  |
| Peaking | 9150 Hz  | 4.39 | -6.1 dB  |
| Peaking | 11251 Hz | 1.16 | 5.6 dB   |
| Peaking | 13324 Hz | 2.44 | -5.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20990%20PRO/Beyerdynamic%20DT%20990%20PRO.png)