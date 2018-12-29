# Beyerdynamic DT 1770 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.0; 28 0.7; 31 0.5; 34 0.3; 37 0.2; 41 0.2; 45 0.2; 49 0.2; 54 0.1; 60 0.0; 66 -0.2; 72 -0.4; 79 -0.7; 87 -1.0; 96 -1.4; 106 -1.8; 116 -2.0; 128 -2.0; 141 -1.7; 155 -1.1; 170 -0.0; 187 1.4; 206 3.0; 227 4.0; 249 3.7; 274 2.1; 302 0.4; 332 -0.8; 365 -1.4; 402 -1.5; 442 -1.3; 486 -1.4; 535 -1.4; 588 -1.4; 647 -1.2; 712 -1.1; 783 -0.8; 861 -0.4; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.3; 1387 0.1; 1526 -0.1; 1678 -0.2; 1846 0.4; 2031 1.0; 2234 0.3; 2457 1.1; 2703 1.9; 2973 2.9; 3270 3.2; 3597 3.2; 3957 4.9; 4353 3.2; 4788 -1.3; 5267 -1.3; 5793 -2.0; 6373 -4.6; 7010 -2.7; 7711 -3.3; 8482 -4.1; 9330 -2.6; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 15 Hz    |  0.15 | 1.2 dB  |
| Peaking | 208 Hz   |  0.53 | -5.0 dB |
| Peaking | 229 Hz   |  1.79 | 9.1 dB  |
| Peaking | 3835 Hz  |  1.66 | 6.1 dB  |
| Peaking | 6350 Hz  |  1.19 | -5.1 dB |
| Peaking | 1117 Hz  |  4.14 | 0.6 dB  |
| Peaking | 4782 Hz  | 12.08 | -2.6 dB |
| Peaking | 8608 Hz  |  0.78 | 1.0 dB  |
| Peaking | 8738 Hz  |  4.13 | -3.3 dB |
| Peaking | 10188 Hz |  3.2  | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201770%20PRO/Beyerdynamic%20DT%201770%20PRO.png)